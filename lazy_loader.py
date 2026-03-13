class LazyModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        if self.model is None:
            print(f"Loading model from {self.model_path}")
            # Logic to load the model
            # self.model = ...
            pass
        else:
            print("Model is already loaded.")

class LoRAManager:
    def __init__(self):
        self.loras = {}

    def add_lora(self, name, lora):
        self.loras[name] = lora
        print(f"Added LoRA: {name}")

    def remove_lora(self, name):
        if name in self.loras:
            del self.loras[name]
            print(f"Removed LoRA: {name}")
        else:
            print(f"LoRA {name} not found.")

    def get_lora(self, name):
        return self.loras.get(name, None)
