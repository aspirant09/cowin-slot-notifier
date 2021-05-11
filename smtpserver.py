import smtplib,ssl
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# set up the SMTP server


def sendMail(receiver,msg,param1,param2):
    subject = ""
    message = MIMEMultipart()
    message["Subject"] = "Cowin slots"
    message["From"] = "abhijithsathyendran@gmail.com"
    message["To"] = receiver
    header="Hello Subscriber, \n\nFollowing centers have slots available for vaccination over the next week \n\n"
    body1=MIMEText(header,'plain')
    body2=MIMEText(msg,'plain')
    message.attach(body1)
    message.attach(body2)
    try:
        print("**"+msg)
        context = ssl.create_default_context()
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls(context=context)
        s.login(param1, param2)
        s.sendmail(param1, receiver,message.as_string())
    
        #s.close()
    except Exception as e:
        print(e)
    finally:
        s.quit()
