#!/usr/bin/env python3

import smtplib
from os import popen
from urllib.request import urlopen

def check():
    # Tests for internet connection, using google.com ip
    try:
        urlopen('http://216.58.192.142', timeout=1)
    except:
        return False
    else:
        return True


def send_Ip():
    sent_from = 'purepytk@gmail.com'
    mail_to = ['purepytk@gmail.com'] # Can send to multiple people, just add another list item
    subject = "RasPi Address"
    body = str(popen("ifconfig | grep inet").read())

    email_text = "Subject: %s\n\n%s" %(subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login("purepytk@gmail.com", "mrexwzbibxoulkcs")
    server.sendmail(sent_from, mail_to, email_text)
    server.close()

if __name__ == '__main__':
    if check():
        send_Ip()
    exit(0)
