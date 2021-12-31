from RPA.Email.ImapSmtp import ImapSmtp
from RPA.Outlook.Application import Application
from RPA.Robocorp.Vault import Vault
import time

def send_gmail_email(recipient, subject, body):
    secret = Vault().get_secret("emailGmailCredentials")
    gmail_account = secret["username"]
    gmail_password = secret["password"]
    mail = ImapSmtp(smtp_server="smtp.gmail.com", smtp_port=587)
    mail.authorize(account=gmail_account, password=gmail_password)
    mail.send_message(
        sender=gmail_account,
        recipients=recipient,
        subject=subject,
        body=body,
    )

def send_outlook_email(recipient, subject, body):
    app = Application()
    app.open_application()
    try:
        app.send_email(recipients=recipient, subject=subject, body=body)
    except Exception as e:
        if e.strerror == 'Call was rejected by callee.':
            time.sleep(2)
            app.send_email(recipients=recipient, subject=subject, body=body)

def get_outlook_email(account_name,folder_name):
    app = Application()
    app.open_application()
    time.sleep(2)
    email_list = app.get_emails(account_name=account_name, folder_name=folder_name, save_attachments=True, attachment_folder="D:\\RobotFramework\\attachments\\")    
    return email_list

# def send_outlook_email(recipient, subject, body):
#     secret = Vault().get_secret("emailOutlookCredentials")
#     outlook_account = secret["username"]
#     outlook_password = secret["password"]
#     mail = ImapSmtp(smtp_server="smtp.office365.com", smtp_port=587)  #should enable smtp access in Exchange
#     mail.authorize(account=outlook_account, password=outlook_password)
#     mail.send_message(
#         sender=outlook_account,
#         recipients=recipient,
#         subject=subject,
#         body=body,
#     )