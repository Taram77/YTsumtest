import anthropic
from bot.Plugins.ClaudeAI import claudeai_prompts as prompts
from bot.Plugins.ClaudeAI import claudeai_models as models
from bot.Plugins import language_helper as languages

class ClaudeAIHelper:
    """
    ClaudeAI helper class.
    """
    def __init__(self, config):
        """
        Initializes the ClaudeAI helper class with the given configuration.
        :param config: A dictionary containing the ClaudeAI configuration
        """
        self.claudeai = anthropic.Anthropic(
            api_key=config['api_key']
        )


    async def get_summary_from_claude(self,text):
        language = languages.recognize_language_from_text(text)
        stream = "The Language was not recognized please provide another URL 🙂"

        if language != "Unknown Language":
            stream = self.claudeai.messages.stream(
                model=models.CLAUDE_3_HAIKU_20240307_MODEL,
                messages=prompts.summarization_2(text, language),
                max_tokens=models.CLAUDE_3_HAIKU_20240307_MODEL_MAX_INPUT_SIZE)

        return stream



