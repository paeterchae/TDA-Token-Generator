from dotenv import load_dotenv
from tda import auth
import os

load_dotenv()

TOKEN_PATH = 'token.json'
API_KEY = os.getenv('API_KEY')
REDIRECT_URI = 'https://localhost'

c = auth.client_from_manual_flow(API_KEY, REDIRECT_URI, TOKEN_PATH)