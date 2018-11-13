# TODO: Получить данные (токен) и выполнить get запрос для активации учетной записи
from tests.tools.request import Request
from tests.tools.variables import *
import imaplib
import re


def get_token_from_email():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('r.babychev@minexsystems.com', 'benjamin100')
    mail.select("INBOX")  # Подключаемся к папке "входящие".
    result, data = mail.uid('search', None, '(FROM "Minex Wallet")')  # Выполняет поиск и возвращает UID писем.
    latest_email_uid = data[0].split()[-1]  # Получить последнее письмо
    result2, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = str(data[0][1])
    t = re.search(r'(?<=token=)(.*=)(?=\">)', raw_email)  # Поиск токена в теле письма
    token = t.string[t.start():t.end()]
    return token


def test_confirm_registration():
    send = Request()
    endpoint = send.get(confirm_register + get_token_from_email())

    assert endpoint.status_code == 200
