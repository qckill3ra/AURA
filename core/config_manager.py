import yaml
from pathlib import Path


class ConfigManager:

    def __init__(self, path="config/config.yaml"):
        self.path = Path(path)
        self.config = self.load()


    def load(self):

        with open(self.path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


    def get(self, section, key):

        return self.config[section][key]