import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pydantic import EmailStr

from src.core.config import settings
from src.core.loggers import utils as logger


def send_email(message: str, to_whom: EmailStr) -> None:
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
        msg["To"] = to_whom
        msg["Subject"] = "Subject of your email"

        body = message
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(sender, to_whom, msg.as_string())
    except Exception as ex:
        logger.error(f"{ex} Check your login or password")
