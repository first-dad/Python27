# -*- coding: utf-8 -*-

import smtplib
from email.message import Message


if __name__ == '__main__':
    fromaddr = "Riamon85@mail.ru"
    toaddrs = ["leroy-wolf@yandex.ru"]
    msg = 'From: %s\r\n To: %s\r\n\r\n\' % (fromaddr, '.' .join(toaddrs))
    msg += """
    Вкладывайте деньги в акции и виагру
    """
    server = smtplib.SMTP('smtp.mail.ru')
    server.login('Riamon85@mail.ru', open('password', 'r').read())
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()