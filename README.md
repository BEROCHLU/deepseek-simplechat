# Chatbot with OpenAI API and DeepSeek  

## Overview  
This script is a simple chatbot that interacts with users using the OpenAI API with DeepSeek. It maintains a conversation history and displays responses in a formatted manner using the `rich` library.  

## Features  
- Uses OpenAI's DeepSeek API for generating responses.  
- Maintains conversation history for context-aware replies.  
- Displays responses in a visually appealing format using `rich`.  

## Requirements  
Ensure you have the following installed:  
- Python 3.11+  
- Required Python packages:  
  ```bash
  pip install openai
  ```  

## Setup  
1. **Set API Key**  
   We can finally top up the DeepSeek API.  
   Export your DeepSeek API key as an environment variable:  
   ```bash
   export DEEPSEEK_API_KEY="your_api_key_here"
   ```  

2. **Run the Script**  
   Execute the script using:  
   ```bash
   python chatbot-rich.py
   ```  

## Usage  
- Type your message and press Enter to interact with the chatbot.  
- The chatbot will respond based on the conversation history.  
- Press Enter without typing anything to exit.  

## Example Interaction  
```plaintext
User: Hello!
Assistant: Hi! How can I assist you today?

User: What is DeepSeek?
Assistant: DeepSeek is an AI model designed for generating intelligent responses...
```

## Configuration  
- Modify the `model` parameter (`deepseek-chat` or `deepseek-reasoner`) to change the response behavior.  
- Adjust `temperature` for response randomness (higher values make responses more creative).  

## Note  
- It takes 30 to 60 seconds to reply to a message.
-  Compared to the OpenAI API, the DeepSeek API costs one-tenth as much.
## License  
MIT