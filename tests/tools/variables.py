"""
BASE URL
"""
origin = "https://webwallet-test.rancher.mnxteam.com"
url = "https://webwallet-test.rancher.mnxteam.com/api/v1.0/"
local_url = "https://webwallet-tester.minikube/api/v1.0/"

"""
NODE URL
"""

address_url = "https://minexcoin-node1.rancher.mnxteam.com/"
cold_url = "https://minexcoin-node2.rancher.mnxteam.com/"
hot_url = "https://minexcoin-node3.rancher.mnxteam.com/"
cold_address = ""
hot_address = ""
my_address = ""


"""
ENDPOINT
"""
register = local_url + "auth/register"
confirm_register = local_url + "auth/validate-email/"
login = url + "auth/login"
transaction = "transactions"
address = "address"
balance = "balance"
send_coin = "address/send"

"""
HEADERS
"""
content_type = 'application/json'
headers = {'Content-Type': content_type}


"""
POST DATA
"""

new_user = '{"email":"r.babychev@minexsystemsgs.com",' \
       ' "password":"Aa123456",' \
       ' "passwordRepeat":"Aa123456",' \
       ' "agreement":true,' \
       ' "captcha":""}'

email = "r.babychev@minexsystems.com"
user = '{"email": "r.babychev@minexsystems.com", "password": "Aa123456", "captcha": ""}'
