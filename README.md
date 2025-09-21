# AI Chatbot with OpenAI GPT-4o-mini

A simple, interactive command-line chatbot powered by OpenAI's GPT-4o-mini model. This chatbot allows you to have conversations with AI directly from your terminal.

## Features

- 🤖 **Interactive Chat Interface**: Continuous conversation loop until you decide to quit
- 🔧 **Configurable Temperature**: Adjustable response creativity (default: 0 for deterministic responses)
- 💰 **Cost-Optimized**: Uses GPT-4o-mini model with limited tokens to minimize API costs
- 🔒 **Secure API Key Management**: Uses environment variables to protect your OpenAI API key
- ⚡ **Error Handling**: Graceful handling of API errors and rate limits

## Prerequisites

- Python 3.7 or higher
- OpenAI API account with available credits
- OpenAI API key

## Installation

1. **Clone or download this project**
   ```bash
   git clone https://github.com/prabinLC/Chatbot.git
   cd Chatbot
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install openai python-dotenv
   ```

4. **Set up your OpenAI API key**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-actual-api-key-here
   ```
   
   **Get your API key from**: [OpenAI Platform](https://platform.openai.com/account/api-keys)

## Usage

1. **Run the chatbot**
   ```bash
   python chatbot.py
   ```

2. **Start chatting**
   - Type your questions or messages when prompted
   - Type `q` or `quit` to exit the conversation

## Example Conversation

```
Ask your ai agent anything, or q to quit !!!!
What is the capital of Nepal?

The capital of Nepal is Kathmandu.

Ask your ai agent anything, or q to quit !!!!
Tell me a joke about programming

Why do programmers prefer dark mode? Because light attracts bugs!

Ask your ai agent anything, or q to quit !!!!
q
```

## Configuration

### Temperature Setting
You can adjust the creativity of responses by modifying the `temperature` parameter in the `get_response_openai()` function:

- **0**: Deterministic, focused responses
- **0.5**: Balanced creativity and consistency  
- **1.0**: More creative and varied responses

### Token Limit
Current setting: `max_tokens=100` (to control costs)
- Increase for longer responses
- Decrease to save on API costs

### Model Selection
Currently using `gpt-4o-mini` for cost efficiency. You can change to:
- `gpt-3.5-turbo`: Faster, cheaper
- `gpt-4`: More capable, more expensive

## File Structure

```
reaction/
├── learn.py          # Main chatbot application
├── .env             # Environment variables (your API key)
├── .gitignore       # Git ignore file (excludes .env)
├── README.md        # This file
└── .venv/           # Virtual environment (if created)
```

## Troubleshooting

### Common Issues

1. **"Module not found" error**
   ```bash
   pip install openai python-dotenv
   ```

2. **"Rate limit exceeded" or "Insufficient quota"**
   - Check your OpenAI account billing: [OpenAI Billing](https://platform.openai.com/account/billing)
   - Add payment method or purchase credits
   - Wait if you've hit rate limits

3. **"Invalid API key"**
   - Verify your API key in the `.env` file
   - Generate a new key if needed: [OpenAI API Keys](https://platform.openai.com/account/api-keys)

4. **No response or hanging**
   - Check your internet connection
   - Verify OpenAI service status

## Security Notes

⚠️ **Important Security Practices:**

- Never commit your `.env` file to version control
- Don't share your API key publicly
- Regenerate your API key if it's been exposed
- The `.gitignore` file is included to prevent accidental commits

## Cost Management

- **Model**: GPT-4o-mini (~$0.15 per 1M input tokens)
- **Max Tokens**: Limited to 100 tokens per response
- **Estimated Cost**: ~$0.001-0.002 per conversation turn

Monitor your usage at: [OpenAI Usage Dashboard](https://platform.openai.com/account/usage)

## Contributing

Feel free to fork this project and submit pull requests for improvements:

- Add conversation history
- Implement different AI personalities
- Add web interface
- Support for different models
- Conversation saving/loading

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your OpenAI account status
3. Review the [OpenAI API documentation](https://platform.openai.com/docs)

---

**Enjoy chatting with your AI assistant!** 🚀