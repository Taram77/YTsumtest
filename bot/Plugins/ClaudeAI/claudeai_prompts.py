

def summarization_2(text, language):
    prompt = [{"role": "user",
      "content": f"please translate the summarization to {language} language"
                 "1.	Write a comprehensive summary of the text. Structure the summary to follow the overall flow of the text. For each major section, summarize the key points, theories, models, frameworks, examples, and insights covered. 
                 Where relevant, provide concrete examples to illustrate the concepts. Summarize any case studies or experiments described in the text. For important terms or theories introduced, explain them clearly and concisely. 
                 Where appropriate, make connections between ideas presented across different chapters or sections. The tone should be professional, neutral and educational. 
                 The length should allow all major aspects of the text to be summarized effectively. The summary should be written to help someone understand the core content of the text in depth."
                 f" Use the text above: {text}."}]
    return prompt

def summarization_3(text, language):
    prompt = [{"role": "user",
      "content": f"please translate the summarization to {language} language"
                "1.	Write a comprehensive summary of the text. Structure the summary to follow the overall flow of the text. For each major section, summarize the key points, theories, models, frameworks, examples, and insights covered. 
                 Where relevant, provide concrete examples to illustrate the concepts. Summarize any case studies or experiments described in the text. For important terms or theories introduced, explain them clearly and concisely. 
                 Where appropriate, make connections between ideas presented across different chapters or sections. The tone should be professional, neutral and educational. 
                 The length should allow all major aspects of the text to be summarized effectively. The summary should be written to help someone understand the core content of the text in depth."
                 f" Use the text above: {text}."}]
    return prompt

