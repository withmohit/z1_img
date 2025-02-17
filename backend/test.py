from dotenv import load_dotenv
import os

load_dotenv()  # Ensure this is before reading the variables
print("CONSUMER_KEY:", os.getenv("X_CLIENT_ID"))  # Debugging check
print("CONSUMER_KEY:", os.getenv("X_CLIENT_SECRET"))  # Debugging check
print("CONSUMER_KEY:", os.getenv("X_ACCESS_TOKEN_SECRET"))  # Debugging check
print("CONSUMER_KEY:", os.getenv("X_ACCESS_TOKEN"))  # Debugging check
