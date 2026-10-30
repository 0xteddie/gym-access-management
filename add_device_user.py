import json
import requests
import base64
import time
from fetch_token import grab_token

"""
Create a new user on the access control device (http://192.168.0.178).

Loads user data from min_user.json and sends it to /api/People/New
as a multipart/form-data request with the field name "PeopleJson".
Requires a valid Bearer token from fetch_token.grab_token().
"""

HOST = "http://192.168.0.178"

def create_or_update_user(person: dict) -> str:
    token = grab_token()

    response = requests.post(
        f"{HOST}/api/People/New",
        headers={
            "Authorization": f"Bearer {token}",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "close",
        },
        files={
            # Important: only two values → no Content-Type header on the part
            "PeopleJson": (None, json.dumps(person, separators=(",", ":")))
        },
    )

    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    with open("min_user.json", "r") as f:
        person = json.load(f)

    print(create_or_update_user(person))
