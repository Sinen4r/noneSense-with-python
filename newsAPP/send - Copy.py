

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email( to):
    sender_email = 'urMAil'
    sender_password = ''  # Use your app password if 2-step verification is enabled

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to
    msg['Subject'] = 'News Update'
    msg.attach(MIMEText('There is an update in the news Section', 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Log in to your account
        server.sendmail(sender_email, to, msg.as_string())  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # Close the connection