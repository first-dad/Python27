# -*- coding: utf-8 -*-

from email.message import Message


if __name__ == '__main__':
    m = Message()
    m.set_charset('utf-8')
    m.add_header('from', 'Ilya')
    m.add_header('To', 'Den')
    m.add_header('subject', 'Test')
    m.set_payload("Hello, body =))", 'utf-8')
    print m