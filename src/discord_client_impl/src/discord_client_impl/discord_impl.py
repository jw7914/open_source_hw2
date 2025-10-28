"""Discord Client Implementation.

This module provides a concrete implementation of the chat client API using the Discord API.
It handles OAuth2 authentication and provides methods to interact with Discord messages.

The implementation supports multiple authentication modes:
    - Environment variables (for CI/CD environments)
    - Local token file (for development)
    - Interactive OAuth flow (for initial setup)
"""
# import chat_client_api
import webbrowser
from urllib.parse import urlencode

import requests

API_ENDPOINT = "https://discord.com/api/v10"
CLIENT_ID = "1432524025564893184"
CLIENT_SECRET = "wZeDPyYyQ7GMOgJ9ODA0T-uq5a38IWcb"
REDIRECT_URI = "http://localhost:8000/callback"
CODE = "eleWqZfmpRHmBxS2hozPS9dvLWg3HX"
AUHTORIZATION_URL =  "https://discord.com/oauth2/authorize?client_id=1432524025564893184&redirect_uri=http%3A%2F%2Flocalhost%3A8000&response_type=code&scope=identify&prompt=consent"
class DiscordClient:

    def __init__(self) -> None:
        params = {
            "client_id": CLIENT_ID,
            "redirect_uri": REDIRECT_URI,
            "response_type": "code",
            "scope": "identify",
        }

        authorize_url = f"https://discord.com/oauth2/authorize?{urlencode(params)}"
        webbrowser.open(authorize_url)

    def exchange_code(self,code):
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        r = requests.post("%s/oauth2/token" % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
        r.raise_for_status()
        return r.json()

        # print(exchange_code(CODE))


    def refresh_token(self,refresh_token):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        r = requests.post("%s/oauth2/token" % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
        r.raise_for_status()
        return r.json()

asd = DiscordClient()
