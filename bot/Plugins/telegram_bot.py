import asyncio
from bot.Plugins.ClaudeAI import claudeai_infrastructure as claudeai
from bot.Plugins import youtube_transcript_api_helper as youtube_transcript_api_helper
from bot.Plugins.OpenAI.openai_infrastructure import OpenAIHelper
import bot.Plugins.OpenAI.openai_models as openai_models
from bot.Plugins.ClaudeAI.claudeai_infrastructure import ClaudeAIHelper
import bot.Plugins.ClaudeAI.claudeai_models as  claudeai_models
from telegram import Update
from telegram.error import RetryAfter
from telegram.ext import Application,CommandHandler, ContextTypes,MessageHandler, filters

class TelegramBot:
    def __init__(self, config,  openai: OpenAIHelper, claudeai: ClaudeAIHelper):
        """
        Initializes the OpenAI helper class with the given configuration.
        :param config: A dictionary containing the GPT configuration
        """
        self.config = config
        self.openai = openai
        self.claudeai = claudeai

    # Define the function to handle the /start command
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Hello 👋 this is the Youtube Summarizer bot,"
                                        " you can send youtube url here for summarization. ")

    async def respond(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_message = update.message.text  # Get the text the user sent to the bot
        message = await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Wait few seconds for processing your request ⏳")

        transcription_text = youtube_transcript_api_helper.youtube_transcript_video(user_message)
        if transcription_text is None or not transcription_text:
            await context.bot.edit_message_text(
                chat_id=update.effective_chat.id,
                message_id=message.message_id,
                text="Something went wrong: check the video, video have no dialog ❌")
        # Use OpenAI to generate a completion based on the user's message

        #texts = [transcription_text[i:i + text_size] for i in range(0, len(transcription_text), text_size)]
        concatenated_content = ""
        #for text in texts:
        text_size = openai_models.GPT_3_5_TURBO_0125_MODEL_SIZE
        stream = await self.openai.get_summary_from_gpt(transcription_text[:text_size])
        content_for_reply = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                concatenated_content += content
                content_for_reply += content
            if len(content_for_reply) > 100:
                try:
                    await context.bot.edit_message_text(
                        chat_id=update.effective_chat.id,
                        message_id=message.message_id,
                        text=concatenated_content)
                except RetryAfter as e:
                    print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")
                    await asyncio.sleep(e.retry_after)
                    # Retry the request after the suggested wait time
                #bot.reply_to(message, content_for_reply)
                content_for_reply = ""

        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text=concatenated_content)
        # Extract the generated text from the OpenAI response
        # Send the OpenAI response as a reply to the user's message

    async def respond_claude(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_message = update.message.text  # Get the text the user sent to the bot
        message = await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Wait few seconds for processing your request ⏳")

        transcription_text = youtube_transcript_api_helper.youtube_transcript_video(user_message)
        if transcription_text is None or not transcription_text:
            await context.bot.edit_message_text(
                chat_id=update.effective_chat.id,
                message_id=message.message_id,
                text="Something went wrong: check the video, video have no dialog ❌")
        # Use ClaudeAI to generate a completion based on the user's message

        claude_stream = await self.claudeai.get_summary_from_claude(
            transcription_text[:claudeai_models.CLAUDE_3_HAIKU_20240307_MODEL_MAX_INPUT_SIZE])

        concatenated_content = ""
        content_for_reply = ""
        with claude_stream as stream:
            for chunk in stream.text_stream:
                content = chunk
                if content:
                    concatenated_content += content
                    content_for_reply += content
                if len(content_for_reply) > 100:
                    try:
                        await context.bot.edit_message_text(
                            chat_id=update.effective_chat.id,
                            message_id=message.message_id,
                            text=concatenated_content)
                    except RetryAfter as e:
                        print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")
                        await asyncio.sleep(e.retry_after)
                        # Retry the request after the suggested wait time
                    #bot.reply_to(message, content_for_reply)
                    content_for_reply = ""

        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text=concatenated_content)

    def run(self):
        application = Application.builder().token(self.config['api_key']).build()
        # Add the command handler to the dispatcher
        application.add_handler(CommandHandler('start', self.start))
        application.add_handler(MessageHandler(filters.TEXT, self.respond_claude))
        # Start the bot
        application.run_polling()
