import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

class Settings:
    model_name: str = os.getenv("MODEL_NAME", "gpt2")
    max_length: int = int(os.getenv("MAX_LENGTH", 50))
    num_return_sequences: int = int(os.getenv("NUM_RETURN_SEQUENCES", 1))

settings = Settings()