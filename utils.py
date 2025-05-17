def load_logs(filepath: str) -> str:
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Could not read logs: {e}"