# Python OOP Assignment 🐍

## 📌 Assignment 1: Design Your Own Class
I created a **Smartphone class** that inherits from a base **Device class**.  
The class includes attributes like `brand`, `model`, `storage`, and `camera`,  
along with methods for taking photos and installing apps.  

### Example Usage
```python
phone1 = Smartphone("Samsung", "Galaxy S24", 256, "108MP")
print(phone1.phone_info())
phone1.take_photo()
phone1.install_app("WhatsApp")
