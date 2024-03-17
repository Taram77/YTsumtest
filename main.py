import os
from dotenv import load_dotenv
from bot.Plugins.OpenAI.openai_infrastructure import OpenAIHelper
from bot.Plugins.ClaudeAI.claudeai_infrastructure import  ClaudeAIHelper
from bot.Plugins.telegram_bot import TelegramBot

def main():
    # Load environment variables from .env file
    load_dotenv()
    # Check if the required environment variables are set
    required_values = ['OPENAI_API_KEY', 'TELEGRAM_API_KEY', 'CLAUDE_API_KEY']
    missing_values = [value for value in required_values if os.getenv(value) is None]
    if len(missing_values) > 0:
        exit(1)

    openai_config = {'api_key': os.getenv('OPENAI_API_KEY')}
    telegram_config = {'api_key': os.getenv('TELEGRAM_API_KEY')}
    claudeai_config = {'api_key': os.getenv('CLAUDE_API_KEY')}

    openai_helper = OpenAIHelper(config=openai_config)
    claudeai_helper = ClaudeAIHelper(config=claudeai_config)
    telegram_bot = TelegramBot(config=telegram_config,
                               openai=openai_helper,
                               claudeai=claudeai_helper)
    telegram_bot.run()

if __name__ == '__main__':
    main()
