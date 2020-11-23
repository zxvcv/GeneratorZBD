import json
from abstract import abstract


class AbstractGenerator:
    def __init__(self, settingsFile):
        self.settings = []
        with open(settingsFile, "r") as f:
            self.settings = json.loads(f.read())

    def generate(self): abstract()

