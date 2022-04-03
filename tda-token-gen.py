from tda import auth

TOKEN_PATH = 'token.json'
#replace "FILL_IN_HERE" with Consumer Key from your TDA Developer App
API_KEY=FILL_IN_HERE@AMER.OAUTHAP
REDIRECT_URI = 'https://localhost'

c = auth.client_from_manual_flow(API_KEY, REDIRECT_URI, TOKEN_PATH)