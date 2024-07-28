# configs.py
import yaml

class ModelConfigs:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            configs = yaml.safe_load(file)
        self.model_path = configs.get('model_path')
        self.vocab = configs.get('vocab')
        self.width = configs.get('width')
        self.height = configs.get('height')
        self.max_text_length = configs.get('max_text_length')
        self.learning_rate = configs.get('learning_rate')
        self.train_epochs = configs.get('train_epochs')
        self.train_workers = configs.get('train_workers')
        self.images = configs.get('images')
        self.labels = configs.get('labels')

    @staticmethod
    def load(config_file):
        return ModelConfigs(config_file)
