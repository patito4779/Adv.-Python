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

