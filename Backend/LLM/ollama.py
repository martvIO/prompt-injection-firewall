from ollama import Client

class AI:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = Client()

    def generate(self, prompt: str) -> str:
        response = self.client.generate(model=self.model_name, prompt=prompt)
        return response['response'] 