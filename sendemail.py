#coiding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os

def mail():
    # mail server
    charset='iso-2022-jp'
    server = 'smtp.gmail.com'

    #login account
    user = 'xxxx@gmail.com'
    password = 'yyyyyyy'

    smtp = smtplib.SMTP(server)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(user, password)

    #mail sending 

    mailFrom = 'xxxxx@gmail.com'
    mailTo = 'yyyyyyy@yahoo.co.jp'

    message = MIMEMultipart()

    message['Subject'] = str(Header('Pythonでメール送信', charset))
    message['From'] = mailFrom
    message['To'] = mailTo

    body = MIMEText(
        'Pythonからの送信です。メールは届きましたか？'.encode(charset),
        'plain',
        charset,
        )
    message.attach(body)

    filePath = os.path.join('directoryName', 'fileName.xls')
    fp = open(filePath, mode='rb')
    m = MIMEApplication(fp.read(), 'vnd.ms-excel')
    fp.close()
    m.add_header("Content-Disposition", "attachment", filename=os.path.basename(filePath))
    message.attach(m)

    smtp.sendmail(
        mailFrom,
        mailTo,
        message.as_string(),
        )
    smtp.close()

if __name__ == '__main__':
    mail()
