from pathlib import Path


class MemoryManager:

    def __init__(self, memory_path="memory"):
        self.memory_path = Path(memory_path)

    def _read(self, filename):

        file = self.memory_path / filename

        if file.exists():
            return file.read_text(encoding="utf-8")

        return ""

    def build_context(self, user_message):

        context = """
Tu es AURA.

Tu es une intelligence artificielle personnelle locale.

Tu ne dois jamais te présenter comme Qwen, un LLM ou un modèle générique.

Réponds toujours comme AURA.

Les informations suivantes constituent ta mémoire permanente.
"""

        files = [
            ("IDENTITÉ", "aura_identity.md"),
            ("SÉCURITÉ", "security.md"),
            ("UTILISATEUR", "user_profile.md"),
            ("HOMELAB", "homelab.md"),
            ("PROJETS", "projects.md"),
        ]

        for title, filename in files:

            content = self._read(filename)

            if content:

                context += f"\n\n===== {title} =====\n"
                context += content

        context += "\n\n===== MESSAGE UTILISATEUR =====\n"
        context += user_message

        return context