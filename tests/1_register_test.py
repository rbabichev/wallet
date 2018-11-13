from tests.tools.request import Request
from tests.tools.variables import *


def test_register():
    send = Request()
    endpoint = send.post(register, new_user, headers)

    # assert endpoint.status_code == 200
    # assert endpoint.headers["Content-Type"] == content_type
    # assert endpoint.headers["Access-control-allow-origin"] == origin
    # assert get_email == email     # убедится что почта не активировани и нет доступа





