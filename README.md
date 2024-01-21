CodeLlama Conversational Chatbot
A simple conversational chatbot built using the codellama/CodeLlama-34b-hf model, which is a large language model trained on a diverse range of programming languages and related texts.

Installation
To install the necessary dependencies, simply run:
bash pip install -r requirements.txt
Usage
Run the following command to start the chatbot:

python3 main.py
The chatbot will greet you and wait for your input. Type your message and press Enter to send it. The chatbot will respond accordingly, and the conversation will continue until the maximum number of lines is reached or you enter an empty line.

Features
Generates responses with beam search (greedy decoding)
Allows up to 10 lines of conversation by default
Displays messages in different colors for better readability
Provides basic error handling for invalid inputs
Limitations
Since this is a code completion model rather than a chatbot model, its responses might sometimes seem irrelevant or off-topic in a conversational context. Additionally, generating long conversations may be slow due to the large size of the model.

Requirements
Python 3.6+
PyTorch >= 1.7.0
Transformers >= 4.9.0
Rich >= 10.8.0
License
MIT License

Contact
If you encounter any issues or would like to contribute to the project, please open an issue or pull request in the GitHub repository at <https://github.com/H4D3ZS/AI_Coder>.

Credits
Based on the work of Hugging Face and Codellama communities. See the full credits in the original repositories:

Hugging Face Transformers Library
Codellama Language Model Repository
