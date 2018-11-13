import imaplib
import re


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('r.babychev@minexsystems.com', 'benjamin100')
mail.select("INBOX")  # Подключаемся к папке "входящие".

result, data = mail.uid('search', None, '(FROM "Minex Wallet")')  # Выполняет поиск и возвращает UID писем.
latest_email_uid = data[0].split()[-1]
result2, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = str(data[0][1])
t = re.search(r'(?<=token=)(.*=)(?=\">)', raw_email)  # Поиск токена в теле письма

print(t.string[t.start():t.end()])



# import email
#
# email_message = email.message_from_bytes(raw_email)
# print("888888888888888888888888888")
# print(type(email_message))
# print("888888888888888888888888888")
# print(email.utils.parseaddr(email_message['To']))
# print(email.utils.parseaddr(email_message['From']))  # получаем имя отправителя
# print(email_message.items())  # Выводит все заголовки.


