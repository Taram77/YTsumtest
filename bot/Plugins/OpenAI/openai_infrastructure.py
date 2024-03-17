
import openai
from . import openai_prompts as prompts
from . import openai_models as models
from .. import language_helper as languages

class OpenAIHelper:
    """
    ChatGPT helper class.
    """
    def __init__(self, config):
        """
        Initializes the OpenAI helper class with the given configuration.
        :param config: A dictionary containing the GPT configuration
        """
        self.openai_helper = openai.OpenAI(api_key=config['api_key'])

    async def get_summary_from_gpt(self,text):
        language = languages.recognize_language_from_text(text)
        stream = "The Language was not recognized please provide another URL 🙂"

        if language != "Unknown Language":
            stream = self.openai_helper.chat.completions.create(
                model=models.GPT_3_5_TURBO_0125_MODEL,
                messages=prompts.summarization_2(text,language),
                stream=True,
            )

        return stream
