import requests
import json


class NodeRPC(object):

    def __init__(self):
        self.request = requests
        self.url = "https://user:password@minexcoin-node1.rancher.mnxteam.com"
        self.header = {'Content-Type': 'application/json'}

    def dumpprivkey(self, address="XWE3dB7aheEErF7Nh2rBXghv8KxoimzEk6"):
        """
        Parameter # 1—the address corresponding to the private key to get
        """
        method = {"method": "dumpprivkey", "params": [address]}
        return self.request.post(self.url, json.dumps(method), self.header)

    def validateaddress(self, address=""):
        """
        Parameter # 1—a P2PKH or P2SH address
        """
        method = {"method": "validateaddress", "params": [address]}
        return self.request.post(self.url, json.dumps(method), self.header)

    def listreceivedbyaddress(self, min_confirm=1):
        """
        Parameter  # 1—the minimum number of confirmations a transaction must have to be counted
        Parameter  # 2—whether to include empty accounts
        Parameter  # 3—whether to include watch-only addresses in results
        Result—addresses, account names, balances, and minimum confirmations
        """
        method = {"method": "listreceivedbyaddress", "params": [min_confirm, True, True]}
        return self.request.post(self.url, json.dumps(method), self.header)

    def sendmany(self, address="XWnphK7LhiRM5kyGbbAhGDWCBngvyCNsEE", amount=0.00000547):
        """
        Parameter # 1—from account ("" as default)
        Parameter # 2—the addresses and amounts to pay
        Parameter # 3—minimum confirmations
        """
        method = {"method": "sendmany", "params": ["", {address: amount}]}
        return self.request.post(self.url, json.dumps(method), self.header)

    def generatetoaddress(self, quantity=1, address="XWnphK7LhiRM5kyGbbAhGDWCBngvyCNsEE"):
        """
        Parameter # 1—how many blocks are generated
        Parameter # 2—the address to send the newly generated coin to
        """
        method = {"method": "generatetoaddress", "params": [quantity, address]}
        return self.request.post(self.url, json.dumps(method), self.header)
