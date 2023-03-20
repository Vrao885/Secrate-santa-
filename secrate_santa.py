from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

load_dotenv()

#Let’s first write a function to send an email using SMTP.

def send_email(sender, receiver, recipient):
    password=os.getenv( 'password')
    body_mgs= f'''\
From:{sender}
subject: your secrate santa present

Hi! Your secret santa is: {recipient}! 🎅
Remember to spend 10$-20$ on your gift, but don't stress about it being the perfect gift!'''

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, body_mgs)


names_list = ['vaishali', 'jay', 'jai', 'vaishu']


names_and_emails = [
  ['vaishali', 'vdah008@gmail.com'],
  ['jay', 'jayrao1991@gmail.com'],
  ['jai', 'jayeshrao@gmail.com'],
  ['vaishu','vaishalirao00@gmail.com']
  
]

if len(names_list) <= 1:
  print('Not enough people to start secret santa!')
  quit()

first_name= names_and_emails[0][0]
while len(names_list) >= 2:
  send_email('<your email here>', names_and_emails[0][1], names_and_emails[1][0])
  names_and_emails.pop(0)
  random.shuffle(names_and_emails)

send_email('<your email here>', names_and_emails[0][1], first_name)
 