
# import pytest
# import pymysql.cursors
import subprocess


args = ["kubectl", "--context", "dev", "-n", "webwallet-test", "port-forward", "deployment.apps/mysql", "3306:3306"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
# print(data)
