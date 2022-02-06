from dotenv import load_dotenv
from tda import auth
import os
from selenium import webdriver

load_dotenv()

token_path = 'token.json'
api_key = os.getenv('API_KEY')
redirect_uri = 'https://localhost'

with webdriver.Chrome() as driver:
    c = auth.client_from_login_flow(
        driver, api_key, redirect_uri, token_path)