# sending email with python smtplib library


# steps to send email
# step 1 -  import 'smtplib' 
# step 2 -  if you want send suject also with email, then import "MIMEMultipart" from "email.mime.multipart" and also import "MIMEText" from email.mime.text
# step 3 -  stor sender email and password into varaible
# step 4  - connect server what you want  ex:- gmail server is -  smtplib.SMTP('smtp.gmail.com',587) 
# step 5 -  call "startls()" method for security
# step 6 -  call login method to email login
# step 7 -  store target emails to send email
# step 8 -  write msg, from, to, body details
# step 9 -  call "send()" method to send emails
# step 10 - call "quit()" method to close the server


#step 1
import smtplib
#step 2
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
#step 3
email = 'rgvarma1950@gmail.com'
pas = '19RGVarma50'
#step 4
s = smtplib.SMTP('smtp.gmail.com',587)     
#step 5
s.starttls()
#step 6
s.login(email,pas)
# step 7
reciever = []
with open('emails_list.txt','r') as f:
    c = f.read().split('\n')
    for x in c:
        reciever.append(x)
    f.close()
print(reciever)
#step 8
msg = MIMEMultipart()
for y in range(len(reciever)):
    msg['From'] = email
    msg['To']   = reciever[y]
    msg['Subject']  =  'I love you'

    body = 'this is a smtp msg send to multiple mails with subject of email'
    msg.attach(MIMEText(body,'plain'))
    txt = msg.as_string()
    #step 9
    s.sendmail(email,reciever[y],txt)
#step 10
s.quit()
print('successfully sent mail with text file')

print('')