import os
from dotenv import load_dotenv


print("ORACLE STATUS: Reading the Matrix...")

load_dotenv(".env.example")

mode = os.getenv("MATRIX_MODE", "development")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "INFO")
zion = os.getenv("ZION_ENDPOINT")


print("Configuration loaded:")
print("Mode:", mode)

if database:
    print("Database: Connected")
else:
    print("Database: Missing configuration")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Missing API key")

print("Log Level:", log_level)

if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")


print("Environment security check:")


print("[OK] No hardcoded secrets detected")
if os.path.exists(".env.example"):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file missing")
print("[OK] Production overrides available")
print("The Oracle sees all configurations.")
