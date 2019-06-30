import json
import hashlib
import requests
import smtplib


# Функция для подсчета md5 - хеш суммы
def md5_hash_sum(url):
    res = requests.get(url)
    # Поднимаем ошибку, если наш реквест был неудачным
    try:
        res.raise_for_status()
    except requests.exception.HTTPError as e:
        return e
    hash_sum = hashlib.md5()
    # Используем метод iter_content, так как мы не знаем насколько большие файлы нам были переданы в Url
    for chunk in res.iter_content(chunk_size=1000000):
        if chunk:
            hash_sum.update(chunk)
    return hash_sum.hexdigest()


# Данные для авторизации (можно вставить свою почту и пароль, сервер и порт)
smtp_server = "smtp.yandex.ru"
smtp_port = 25
smtp_email = "dankol@yandex.ru"
smtp_password = "102030"


# Функция для отправки email'а по адресу из нашего POST'а
def send_email(email, msg):
    mail_lib = smtplib.SMTP(smtp_server, smtp_port)
    try:
        mail_lib.login(smtp_email, smtp_password)
    except SMTPAuthenticationError:
        return
    mail_lib.sendmail(smtp_email, email, msg)
    mail_lib.quit()


# Функция создания json файлов в качестве нашей "базы данных"
def create_json(id, status, url, md5='None', email='None'):
    # Создаем задачу для текущего запроса
    task = {
        'id': id,
        'url': url,
        'status': status,
        'md5': md5,
        'email': email
    }
    # Создаем файл с именем <id нашего запроса>.json и записываем в него нашу задачу
    with open(id + ".json", 'w') as inf:
        json.dump(task, inf, indent=4)
