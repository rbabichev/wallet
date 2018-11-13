# import pytest
#
#
# def parrot(i):
#     return i
#
#
# @pytest.mark.parametrize('inp, expected', [("d", "a"), (1, 1), (2, 2), (4, 4)])
# def test_parrot(inp, expected):
#     assert parrot(inp) == expected



from login_test import test_login


print(test_login())
