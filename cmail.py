import smtplib
from email.message import EmailMessage
#from smtplib import SMTP_SSL
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('pradeepraghavendra47@gmail.com','dddlgpqipnlbcnhh')
    msg=EmailMessage()
    msg['From']='pradeepraghavendra47@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()