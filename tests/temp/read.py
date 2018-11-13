import re
# from tests.saved_token import token
result = 0
with open("saved_token.py", "r") as f:

    for i in f:
        result = re.findall(r'token = ".*="$')

print(result)
# with open("saved_token.py", "a") as d:
#     result = d.write("sdfsdfsdfsdf")


# with open("saved_token.py", "w") as z:
#     d = z.write("dddd")
    # read_token = re.findall('^\".*=\"$', token)
    # print(read_token)
    # f.write('token = ' + '"' + read_token + '"')
    # f.write('token = ' + '"' + save_token + '"')
#
# import re
# test_str = 'token = "JFwZaNvNaJNJNwttnJc7WfdFgpY2nIdwfWYkxnlI42U"'
# result = re.findall(r'^token = ".*"$', test_str)
# print(result)



XWE3dB7aheEErF7Nh2rBXghv8KxoimzEk6

KwRBY7k7MfnmpPTSZr6mvkWwiERekgggnzSzrDEPp8rKhW2tuYcm
