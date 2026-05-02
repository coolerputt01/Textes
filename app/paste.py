import os
import sys

# 1. Add the DLL directory
dll_dir = r'C:\Users\Coolerputt\Documents\Textes\app\modules'
os.add_dll_directory(dll_dir)

# 2. Add the parent folder to sys.path so Python can see the 'modules' package
sys.path.append(r'C:\Users\Coolerputt\Documents\Textes\app')

try:
    from modules import services
    print("Success! Services loaded.")
    # Test a function
    s = services.dbInit("./test.db")
    print("DB Initialized.")
except Exception as e:
    print(f"Failed: {e}")
