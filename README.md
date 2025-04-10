# A terminal chatbot using the DeepSeek API  

## Overview  
This script is a simple chatbot that interacts with users through a terminal using the DeepSeek API. It maintains and saves conversation history.  

## Features  
- Uses DeepSeek API for generating responses.  
- Maintains conversation history for context-aware replies.  
- Saves conversation history to the `./history` folder.  
- Supports text files content input using pipe`␣|␣` syntax.  

## Requirements  
Ensure you have the following installed:  
- Python 3.10+  
- Required Python packages:  
  ```bash
  pip install openai
  ```  
  According to public documentation, the DeepSeek API is compatible with OpenAI.  

Optional (recommended):
- [Windows Terminal](https://apps.microsoft.com/detail/windows-terminal/9N0DX20HK701)  
  Clearly renders text, prevents corrupted text, and eliminates screen artifacts.  

## Setup  
1. **Set API Key**  
   Export your DeepSeek API key as an environment variable:  
   ```bash
   export DEEPSEEK_API_KEY="your_api_key_here"
   ```  

2. **Run the Script**  
   - Execute the script using:  
   ```bash
   python chatbot-deepseek.py
   ```  
   - Optional (Windows users):  
   You may use the provided batch script (`script/wt-deepseek.bat`) to launch the chatbot quickly via Windows Terminal.  

## Usage  
Basic chat:

    User: Your question

File analysis mode: (Use spaces around '|' and multiple files supported.)

    User: Explain this code | /path/to/example.py | /path/to/another_file.py

Exit: Press Enter with empty input to save the conversation history to `./history` folder.

## Example Interaction  
```plaintext
User: What is DeepSeek?
Assistant:
DeepSeek Artificial Intelligence Co., Ltd. (referred to as "DeepSeek" or "深度求索") , founded in 2023, is a Chinese company dedicated to making AGI a reality.

User: Help fix this error | err_log.txt
Assistant:
### Error Analysis
The contents of `err_log.txt` indicate the following issues...

User: Suggest optimizations | history/main.py
Assistant:
# Optimized code example here...

User: Translate please | a.txt | history/b.txt | c.txt
Assistant:
# Translated text here...
```

## Configuration  
- **model**: Choose between `deepseek-chat` or `deepseek-reasoner`.  
- **temperature**: Controls randomness. Refer to [official docs](https://api-docs.deepseek.com/quick_start/parameter_settings) for valid ranges.  
- **max_tokens**: For both models, 8192 is the maximum for now.
- **reasoning_effort**: Apparently, this parameter will be available soon.  

## Note  
- The DeepSeek API is more stable compared to the browser version and allows specifying a maximum token limit of up to 8K.
- As a reasoner model, the DeepSeek API costs one-hundredth as much as the OpenAI API.  

## License  
MIT