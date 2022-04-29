"""
Get all the keys contents of an email messages and log it out to an external text file
"""
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys

username = sys.argv[1]
password = sys.argv[2]

imap = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
# Authenticate login creds
imap.login(username, password)

status, messages = imap.select("Inbox")
messages = int(messages[0])
print(messages)

# Initialize a variable n for the number of top emails to be read, let's say the first 10 emails
n = 10
for i in range(messages, 0, -1):
    
