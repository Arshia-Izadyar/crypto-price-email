import smtplib
from main import msg


MESSAGE = msg()
gmail_user = "YOU'R EMAIL"
gmail_password = "APPS PASSWORD"


def send_mail():

    sent_from = gmail_user
    to = ["EMAIL"]
    subject = 'Price :) '
    body = MESSAGE

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print('ERROR !!! ', ex)


if __name__ == "__main__":
    send_mail()
