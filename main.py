\
    #!/usr/bin/env python3
    """Beseri-AI CLI — revamped, clean, and open-source replacement core.

    Features:
    - Clean core (BeseriAi) reimplementation
    - Animated solving indicator
    - History saving (history.json)
    - Web preview generation
    - Professional ASCII banner
    """
    import os
    import sys
    import time
    import threading
    import json
    import webbrowser
    from core import BeseriAi, Log
    from core import parser as CoreParser

    HERE = os.path.dirname(os.path.abspath(__file__))
    PROMPT_FILE = os.path.join(HERE, "system-prompt.txt")
    HISTORY_FILE = os.path.join(HERE, "history.json")
    proxy = os.getenv("BESERI_PROXY") or os.getenv("GROK_PROXY", "")

    ASCII_HEADER = (
        "  ____                  _        _      _     \\n"
        " |  _ \\ __ _ _ __   ___| | _____| | ___(_)___ \\n"
        " | |_) / _` | '_ \\ / _ \\ |/ / _ \\ |/ _ \\ / __|\\n"
        " |  __/ (_| | | | |  __/   <  __/ |  __/ \\__ \\ \\n"
        " |_|   \\__,_|_| |_|\\___|_|\\_\\___|_|\\___|_|___/\\n"
        "                                                  \\n"
        "                 Beseri-AI CLI                    \\n"
    )

    _anim_stop = False

    def start_solving_animation(label="Processing..."):
        global _anim_stop
        _anim_stop = False
        frames = ["⠁", "⠂", "⠄", "⠂"]
        def animate():
            while not _anim_stop:
                for frame in frames:
                    if _anim_stop:
                        break
                    sys.stdout.write(f"\\r{frame} {label}")
                    sys.stdout.flush()
                    time.sleep(0.12)
        threading.Thread(target=animate, daemon=True).start()

    def stop_solving_animation(done_text="✓ Completed."):
        global _anim_stop
        _anim_stop = True
        sys.stdout.write(f"\\r{done_text}{' ' * 20}\\n")
        sys.stdout.flush()

    def print_header():
        try:
            print(ASCII_HEADER)
        except Exception:
            pass

    def get_system_prompt():
        return CoreParser.load_system_prompt(PROMPT_FILE)

    def save_history(entry: dict):
        hist = []
        try:
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                    hist = json.load(f)
        except Exception:
            hist = []
        hist.append(entry)
        try:
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(hist, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def send_message(client: BeseriAi, message: str, extra_data: dict | None):
        if not extra_data:
            sp = get_system_prompt()
            extra_data = {"system_prompt": sp} if sp else None
        try:
            res = client.start_convo(message, extra_data=extra_data)
            if isinstance(res, dict):
                return res.get("response"), res.get("extra_data")
            return str(res), extra_data
        except Exception as e:
            Log.Error(f"Beseri-AI error: {e}")
            return f"[Beseri-AI Error] {e}", extra_data

    def web_preview(text: str, filename="beseriai_response.html"):
        path = os.path.join(HERE, filename)
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("<html><body><pre>" + text.replace("<", "&lt;").replace(">", "&gt;") + "</pre></body></html>")
            webbrowser.open("file://" + path)
        except Exception as e:
            Log.Error(f"Failed to write web preview: {e}")

    def main():
        print_header()
        client = BeseriAi(proxy)
        extra_data = None
        last_response = ""
        print("Commands: /exit /restart /web /proxy <url> /history")
        while True:
            try:
                msg = input("> ").strip()
                if not msg:
                    continue
                if msg == "/exit":
                    return
                if msg == "/restart":
                    extra_data = None
                    print("Conversation restarted.")
                    continue
                if msg.startswith("/proxy "):
                    proxy_url = msg.split(maxsplit=1)[1]
                    client = BeseriAi(proxy_url)
                    extra_data = None
                    print(f"Proxy set to {proxy_url} and conversation restarted.")
                    continue
                if msg == "/web":
                    if not last_response:
                        print("No response yet to show in web view.")
                        continue
                    web_preview(last_response)
                    continue
                if msg == "/history":
                    try:
                        if os.path.exists(HISTORY_FILE):
                            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                                data = json.load(f)
                                for i, e in enumerate(data[-20:], start=1):
                                    print(f"[{i}] {e.get('user')}: {e.get('response')[:120].replace('\\n',' ')}")
                        else:
                            print("No history yet.")
                    except Exception as e:
                        Log.Error(f"Failed reading history: {e}")
                    continue

                start_solving_animation("Processing...")
                response, extra_data = send_message(client, msg, extra_data)
                stop_solving_animation()

                last_response = response or ""
                print("\n" + last_response + "\n")
                save_history({'user': msg, 'response': last_response, 'time': time.time()})
            except KeyboardInterrupt:
                print("\\nInterrupted — exiting.")
                return

    if __name__ == "__main__":
        main()
