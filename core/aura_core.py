import ollama


class AuraCore:

    def __init__(self, model):
        self.model = model


    def ask(self, message):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content":
                    """
                    Tu es AURA.
                    Assistante IA locale sécurisée.
                    Tu demandes confirmation avant toute action.
                    """
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]