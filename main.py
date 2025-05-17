from summarizer.agent import summarize_incident
from utils import load_logs

def main():
    logs = load_logs("data/sample_logs.txt")
    summary = summarize_incident(logs)
    print("\n--- Incident Summary ---\n")
    print(summary)

if __name__ == "__main__":
    main()