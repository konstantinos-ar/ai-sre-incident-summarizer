from summarizer.prompt_templates import INCIDENT_SUMMARY_TEMPLATE
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_incident(logs: str) -> str:
    prompt = INCIDENT_SUMMARY_TEMPLATE.format(logs=logs)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error during summarization: {e}"