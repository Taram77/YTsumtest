

def summarization_2(text, language):
    prompt = [{"role": "user",
      "content": f"please translate the summarization to {language} language"
                 "Your output should use the following template:"
                 "### Summary"
                 "### Analogy"
                 "### Notes"
                 "- [Emoji] Bulletpoint"
                 "### Keywords"
                 "- Explanation"
                 "You have been tasked with creating a concise summary of a YouTube video using its transcription."
                 "Make a summary of the transcript."
                 "Additionally make a short complex analogy to give context and/or analogy from day-to-day life from the transcript."
                 "Create 10 bullet points (each with an appropriate emoji) that summarize the key points or important moments from the video's transcription."
                 "In addition to the bullet points, extract the most important keywords and any complex words not known to the average reader aswell as any acronyms mentioned."
                 " For each keyword and complex word, provide an explanation and definition based on its occurrence in the transcription."
                 f"Please ensure that the summary, bullet points, and explanations fit within the 330-word limit, while still offering a comprehensive and clear understanding of the video's content."
                 f" Use the text above: {text}."}]
    return prompt

def summarization_3(text, language):
    prompt = [{"role": "user",
      "content": f"please translate the summarization to {language} language"
                 "Your output should use the following template:"
                 "### Summary"
                 "### Analogy"
                 "### Notes"
                 "- [Emoji] Bulletpoint"
                 "### Keywords"
                 "- Explanation"
                 "You have been tasked with creating a concise summary of a YouTube video using its transcription."
                 "Make a summary of the transcript."
                 "Additionally make a short complex analogy to give context and/or analogy from day-to-day life from the transcript."
                 "Create 10 bullet points (each with an appropriate emoji) that summarize the key points or important moments from the video's transcription."
                 "In addition to the bullet points, extract the most important keywords and any complex words not known to the average reader aswell as any acronyms mentioned."
                 " For each keyword and complex word, provide an explanation and definition based on its occurrence in the transcription."
                 f"Please ensure that the summary, bullet points, and explanations fit within the 330-word limit, while still offering a comprehensive and clear understanding of the video's content."
                 f" Use the text above: {text}."}]
    return prompt

