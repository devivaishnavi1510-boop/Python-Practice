class Laptop:
    storage_type = "SSD"
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    def get_info(self):
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Type: {self.storage_type}")


l1 = Laptop("16g", "512gb")
l2 = Laptop("8g", "256gb")
l1.get_info()
l2.get_info()