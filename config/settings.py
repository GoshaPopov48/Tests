from dotenv import load_dotenv
import os


load_dotenv()

class Settings:
    
    BASE_URL = os.getenv("BASE_URL")
    API_TOKEN = os.getenv("API_TOKEN")