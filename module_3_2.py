#"Способы вызова функции"


def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    if (('@' and ('.com' or '.ru' or '.net')) not in (recipient or sender)
            or ('@' or ('.com' or '.ru' or '.net')) not in (sender or recipient)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender = 'university.help@gmail.com')

