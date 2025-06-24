
# strava_auth.py
# Vul hier je eigen Strava Client ID en Secret in

CLIENT_ID = "jouw_client_id"
CLIENT_SECRET = "jouw_client_secret"

def get_auth_url(redirect_uri):
    return f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={redirect_uri}&approval_prompt=force&scope=activity:read"

def exchange_token(code):
    import requests
    response = requests.post("https://www.strava.com/oauth/token", data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code"
    })
    return response.json()
