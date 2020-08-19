import smtplib
from email.mime.text import MIMEText


def send_mail(customer,comments):
    port = 465
    smtp_server = 'smtp.sendgrid.net'
    login = 'apikey'
    password = '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'
    message = f"<h3>Vidveda Test</h3><ul><li>Customer: {customer}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'info@walkwithanirudh.site'
    receiver_email = f"{customer}"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'VID VEDA TEST MAIL'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
