# A terminal chatbot using the DeepSeek API.  

## Overview  
This script is a simple chatbot that interacts with users through a terminal using the DeepSeek API. It maintains a conversation history and displays responses in a formatted manner using the `rich` library.  

## Features  
- Uses DeepSeek API for generating responses.  
- Maintains conversation history for context-aware replies.  
- Displays responses in a visually appealing format using `rich` library.  
- Ollama or Hugging Face are not required.

## Requirements  
Ensure you have the following installed:  
- Python 3.11+  
- Required Python packages:  
  ```bash
  pip install openai
  ```  
  According to public document of DeepSeep API, the DeepSeek API uses an API format compatible with OpenAI.  

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
User: What is DeepSeek?
Assistant:
DeepSeek Artificial Intelligence Co., Ltd. (referred to as "DeepSeek" or "深度求索") , founded in 2023, is a Chinese company dedicated to making AGI a reality.

User:
```

## Configuration  
- Modify the `model` parameter (`deepseek-chat` or `deepseek-reasoner`) to change the response behavior.  
- For `temperature` adjustments, refer to [the DeepSeek public docs](https://api-docs.deepseek.com/quick_start/parameter_settings).  

## Note  
- It takes 30 to 60 seconds to reply to a message.
-  Compared to the OpenAI API, the DeepSeek API costs one-tenth as much.
## License  
MIT