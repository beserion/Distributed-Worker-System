import time
import json
from .logger import Log

class BeseriAi:
    """A lightweight replacement for the protected WormAi class.
    Provides start_convo(message, extra_data) -> dict with 'response' and optional 'extra_data'.
    This implementation is synchronous and simple; replace with real model integration as needed.
    """
    def __init__(self, proxy: str = ''):
        self.proxy = proxy
        Log.Info(f"BeseriAi initialized (proxy={proxy})")

    def start_convo(self, message: str, extra_data: dict | None = None):
        """Simulate processing and return a structured response.
        If extra_data contains 'system_prompt', incorporate it.
        """
        Log.Info("Processing message in BeseriAi.start_convo...")
        # Simulate some work
        time.sleep(0.35)
        system_prompt = (extra_data or {}).get('system_prompt') if extra_data else None
        response_text = self._generate_response(message, system_prompt)
        return {'response': response_text, 'extra_data': extra_data}

    def _generate_response(self, message: str, system_prompt: str | None):
        # Very simple response generator — replace with real model calls.
        if system_prompt:
            return f"[System Prompt Applied] {system_prompt}\n>> {message}\n(Reply: This is a simulated response from Beseri-AI.)"
        return f"Echo: {message}\n(Reply: This is a simulated response from Beseri-AI.)"
