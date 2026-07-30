import ollama


class LLMManager:

    def __init__(self, model):
        self.model = model


    def ask(self, message):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]