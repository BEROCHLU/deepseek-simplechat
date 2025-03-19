# A terminal chatbot using the DeepSeek API  

## Overview  
This script is a simple chatbot that interacts with users through a terminal using the DeepSeek API. It maintains a conversation history and displays responses in a formatted manner using the `rich` library.  

## Features  
- Uses DeepSeek API for generating responses.  
- Maintains conversation history for context-aware replies.  
- Supports file content input using `::` syntax.  
- Displays responses in a visually appealing format using `rich` library.  
- Ollama or Hugging Face are not required.  

## Requirements  
Ensure you have the following installed:  
- Python 3.10+  
- Required Python packages:  
  ```bash
  pip install openai
  ```  
  According to public document of DeepSeep API, the DeepSeek API uses an API format compatible with OpenAI.  

## Setup  
1. **Set API Key**  
   Export your DeepSeek API key as an environment variable:  
   ```bash
   export DEEPSEEK_API_KEY="your_api_key_here"
   ```  

2. **Run the Script**  
   Execute the script using:  
   ```bash
   python chatbot-deepseek.py
   ```  

## Usage  
 Basic chat:

    User: Your question
   
 File analysis mode:
   
    User: Explain this code::/path/to/example.py
   
 Exit: Press Enter with empty input and then conversation history was saved history folder.

## Example Interaction  
```plaintext
User: What is DeepSeek?
Assistant:
DeepSeek Artificial Intelligence Co., Ltd. (referred to as "DeepSeek" or "深度求索") , founded in 2023, is a Chinese company dedicated to making AGI a reality.

User: Help fix this error::error_log.txt
Assistant:
### Error Analysis
The contents of `error_log.txt` indicate the following issues...

User: Suggest optimizations::history/main.py
Assistant:
# Optimized code example here
```

## Configuration  
- **Model**: Choose between `deepseek-chat` or `deepseek-reasoner`.  
- **Temperature**: Controls randomness. Refer to [official docs](https://api-docs.deepseek.com/quick_start/parameter_settings) for valid ranges.  
- **reasoning_effort**: Apparently, this parameter will be available soon.  

## Note  
- Replying to a message takes at least 30 seconds.  
- As a reasoner model, the DeepSeek API costs one-hundredth as much as the OpenAI API.  

## License  
MIT