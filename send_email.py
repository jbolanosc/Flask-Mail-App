import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'dbd5d542281ed5'
    password = '605eef8b77efde' 
    message = f"<h3>New Feedback submission </h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Toyota Rent Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver, msg.as_string()) 