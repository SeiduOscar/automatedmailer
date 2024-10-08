import time 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

recipient = input("Enter receipient's address: ")
sender ='elquabatsbot@gmail.com'
senderpassword = 'eyyp apnm gkxz tvrj'
subject_input = input("Enter the message Subject: ").upper()
message_body = input("Message body: ")
message_time = time

messgae_to_send = f"{subject_input}\n{message_body}"

sender_email = sender
sender_password = senderpassword
receiver_email = recipient


subject = subject_input
body = f"""
{message_body}
"""

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))


try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    server.quit()  

#app password = eyyp apnm gkxz tvrj
