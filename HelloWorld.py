import ctypes  # An included library with Python install.

ctypes.windll.user32.MessageBoxW(0, "Hello World!", "Da Bomb Text Box", 1)