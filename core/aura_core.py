from core.config_manager import ConfigManager
from core.llm_manager import LLMManager
from core.memory_manager import MemoryManager


class AuraCore:

    def __init__(self):

        # Configuration
        self.config = ConfigManager()

        # Mémoire
        self.memory = MemoryManager()

        # Modèle IA
        model = self.config.get("llm", "model")

        # LLM
        self.llm = LLMManager(model)

    def ask(self, user_message):

        # Construction du contexte complet
        prompt = self.memory.build_context(user_message)

        # Envoi au LLM
        return self.llm.ask(prompt)