#! /usr/bin/env python

import smtplib, commands
from email.mime.text import MIMEText
import os
import paramiko

host="x.x.x.x"
port=22
user="admin"
password="xxxxxxxxxx"
def send(body, txt):
    print "start"
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    gmail_user = "xxxxxxx@gmail.com"
    gmail_pwd = "xxxxxxxx"
    mailServer.login(gmail_user, gmail_pwd)
    msg = MIMEText(txt)
    msg['From'] = gmail_user
    msg['To'] = 'abcd@gmail.com'
    msg['Subject'] = "Database Backup Falied - " + body
    mailServer.sendmail(msg['From'], msg['To'], msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

def make_backup(local,remote):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
    except:
        print "server-could-not-be-connected"
        raise

    try:
        sftp.put(local, remote)
    except:
        print "damaged-file-path"
        raise

    sftp.close()
    transport.close()

def backup_commands():
    '''
    Doing db backup here
    '''
    return file
make_backup('/home/piyush/ab.py','/home/kadmin/aa.py')
send("Done","")

