import sys
import os
import site


venv_name = os.environ.get("VIRTUAL_ENV")
if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You’re still plugged in")

    print("Current Python:", sys.executable)
    print("Virtual Environment:", venv_name, "detected")
    print("WARNING: You’re in the global environment!\n"
          "The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print()
    print("Then run this program again.")

if sys.prefix != sys.base_prefix:
    print("MATRIX STATUS: Welcome to the construct")
    print("Current Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)
    print()
    print("SUCCESS: You’re in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system.")
    print("Package installation path:")
    print(site.getsitepackages())
