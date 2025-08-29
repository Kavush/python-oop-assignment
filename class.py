# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.camera = camera

    def take_photo(self):
        print(f"Taking a photo with {self.camera} camera...")

    def install_app(self, app):
        print(f" Installing {app} on {self.device_info()}...")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Camera: {self.camera}"


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, "108MP")
phone2 = Smartphone("Apple", "iPhone 15", 512, "48MP")

# Testing methods
print(phone1.phone_info())
phone1.take_photo()
phone1.install_app("WhatsApp")

print(phone2.phone_info())
phone2.take_photo()
phone2.install_app("Instagram")
