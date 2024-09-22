import os

def clear():
    """Bersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
