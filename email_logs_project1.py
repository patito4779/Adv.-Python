"""
Get all the keys contents of an email messages and log it out to an external text file
"""
import re
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import sys
def naming(text):
     return "".join(c if c.isalnum() else "_" for c in text)
path = os.getcwd()
print(path)

username = sys.argv[1]
password = sys.argv[2]

imap = imaplib.IMAP4_SSL("imap.mail.yahoo.com")
# Authenticate login creds
imap.login(username, password)

status, messages = imap.select("Inbox")
messages = int(messages[0])
print(messages)

# Initialize a variable n for the number of bottom emails to be read, let's say the last 10 emails in our Inbox Folder
n = 10
for i in range(1, messages-(messages-n+1), 1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    #file = open(path + "/patrick_email_logs.txt", "w")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            #str(print(dir(msg))) + "\n" + str(print(msg.keys())) # This line prints the methods and keys available with the msg function
            
            for key in msg.keys():
                key = key.rstrip()
                keys, encoding = decode_header(msg.get(key))[0]
                try: 
                    if isinstance(keys, bytes):
                        keys = key.decode(encoding)
                except: keys = key.encode(encoding)
                print(key + ":", keys, end = "\n")
            

            if msg.is_multipart():
                # iterating over the parts of the email
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the body of the email
                        body = part.get_payload(decode=True).decode("utf-8")
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        
                        # print text/plain emails and skip attachments
                        print(body)
                    elif "attachment" in content_disposition:
                        # download to a folder in current working directory
                        filename = part.get_filename()
                        if filename:
                            for key in msg.keys():
                                if key == "Subject":
                                    keys, encoding = decode_header(msg.get(key))[0]
                                    if isinstance(keys, bytes):
                                        keys = keys.decode(encoding)
                                
                            foldername = naming(keys)
                            if not os.path.isdir(foldername):
                                # make a folder for this email (named after the subject)
                                os.mkdir(foldername)
                            filepath = os.path.join(foldername, filename)
                            # download attachment and save it
                            open(filepath, "wb").write(part.get_payload(decode=True))
            
            else:
            # extract content type of email
                content_type = msg.get_content_type()
                body = msg.get_payload(decode=True).decode("utf-8")
                if content_type == "text/plain":
                    print(body.encoding("utf-8"))
            
            if content_type == "text/html":
                pass

            print("="*100)

imap.close()
imap.logout()


            
            

    
    
