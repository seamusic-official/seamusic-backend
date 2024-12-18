import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.infrastructure.config import settings
from src.infrastructure.loggers import infrastructure as logger


def send_email(message: str, recipient: str, subject: str) -> None:
    sender = settings.email_address
    password = settings.email_password

    smtp_server = settings.smtp_host
    smtp_port = settings.smtp_port

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)

        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject

        body = message
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(sender, recipient, msg.as_string())
    except Exception as ex:
        logger.error(f"{ex}, Maybe, incorrect login or password")
