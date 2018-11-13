from tests.tools.btc_rpc import NodeRPC
import json


def test_getinfo():
    send = NodeRPC()
    endpoint = send.listreceivedbyaddress()
    print(json.dumps(json.loads(endpoint.text), indent=4))
    #assert endpoint.status_code == 200


def test_dumpprivkey():
    send = NodeRPC()
    endpoint = send.dumpprivkey()
    print(json.dumps(json.loads(endpoint.text), indent=4))
    #assert endpoint.status_code == 200


def test_generate():
    send = NodeRPC()
    endpoint = send.generatetoaddress(4, "XWnphK7LhiRM5kyGbbAhGDWCBngvyCNsEE")
    print(json.dumps(json.loads(endpoint.text), indent=4))
    #assert endpoint.status_code == 200

