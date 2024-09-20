import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "mollayev.tima@mail.ru"
toaddr = "mollayev.tima@mail.ru"
mypass = "zyNjfyAFGXNU8xP06PU0"
reportname = 'new.html'

msg = MIMEMultipart()
msg['from'] = fromaddr
msg['to'] = toaddr
msg['Subject'] = 'Привет'
with open(reportname, 'rb') as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = "attachment'; filename='%s'" % basename(reportname)
    msg.attach(part)

body = 'Тесты завершены'
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

