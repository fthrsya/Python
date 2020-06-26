import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("email", "pass")

    mesaj = MIMEMultipart()
    mesaj["From"] = "from email"           
    mesaj["To"] = "to email"
    mesaj["Subject"] = "Python email send"    



    body = """

    Python Email

    """

    body_text = MIMEText(body, "plain")  #
    mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("success.")
    mail.close()


except:
    print("Error:", sys.exc_info()[0])
