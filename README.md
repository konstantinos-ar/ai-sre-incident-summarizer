# AI SRE Incident Summarizer

This project uses a language model (OpenAI GPT or local model via Ollama) to summarize incident logs and generate root cause hypotheses and remediation steps.

## How it Works
- Load logs or alerts (e.g., from Honeycomb)
- Generate summaries and actionable insights using an LLM
- Outputs structured summaries for engineering and SRE teams

## Getting Started
Install dependencies:
```bash
pip install -r requirements.txt
Run the summarizer:
python main.py
#### 📄 `requirements.txt`
```txt
openai==1.14.3