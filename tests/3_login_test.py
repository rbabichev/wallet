from tests.tools.request import Request
from tests.tools.variables import *


def test_login():
    send = Request()
    endpoint = send.post(login, user, headers)

    save_token = endpoint.json().get("data").get("accessToken")  # save accessToken for next requests
    with open("tools/saved_token.py", "a") as f:
        f.write('token = ' + '"' + save_token + '"')

    get_email = endpoint.json().get("data").get("email")  # get email from response

    # assert endpoint.status_code == 200
    # assert endpoint.headers["Access-control-allow-origin"] == origin
    # assert endpoint.headers["Content-Type"] == content_type
    # assert get_email == email
