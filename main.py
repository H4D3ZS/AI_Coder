import sys
import time
import random
import torch
from rich import print as rprint
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-34b-hf")
model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-34b-hf").half().cuda()

# Set maximum number of lines to generate
max_lines = 10

# Initialize conversation history
history = ["<human>: Hello!\n"]

while True:
    # Encode current conversation history
    input_ids = torch.tensor(tokenizer.encode(history[-1], return_tensors="pt")).unsqueeze(0).cuda()

    # Generate response with beam search (greedy decoding)
    output = model.generate(
        input_ids=input_ids,
        max_length=100,
        num_beams=5,
        early_stopping=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.bos_token_id,
    )

    # Decode generated tokens back into text
    response = tokenizer.decode(output[0]).strip()

    # Add generated response to conversation history
    history.append("<bot>: {}".format(response))

    # Print out generated response
    rprint("[bold green][Bot]: {}".format(response))

    # Check if maximum number of lines has been reached
    if len(history) > max_lines:
        break

    # Get user input
    while True:
        try:
            user_input = input("\n[bold blue](You): ")
            if not user_input:
                raise ValueError
            break
        except KeyboardInterrupt:
            continue
        except EOFError:
            print("\nGoodbye!")
            sys.exit()
        except Exception as e:
            print("Invalid input.")

    # Add user input to conversation history
    history.append("<human>: {}".format(user_input))

    # Print out user input
    rprint("[bold blue](You): {}".format(user_input))

rprint("\nConversation ended.\n")