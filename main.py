import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from requesthandler import api_request
from timeconvert import time_from_to
from dotenv import load_dotenv
load_dotenv()
import logging


logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_previous_assignments():
    try:
        with open('previous_assignments.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save newly retrieved assignments to a file
def save_assignments(assignments):
    with open('previous_assignments.json', 'w') as file:
        json.dump(assignments, file)

# Function to send email notification
def send_email(recipient, subject, message):
    sender_email = os.getenv("SMTP_USERNAME")
    sender_password = os.getenv("SMTP_PASSWORD")

    # Create a secure SSL context
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)
        logging.info("Email Sent")

# Main function
def main():

    try:
        time_from, time_to= time_from_to()
        assignments = api_request(time_from,time_to)
        print("Assignments",assignments)
        previous_assignments = load_previous_assignments()


        new_assignments = []
        for assignment in assignments:
            # Check if the assignment is new
            if assignment not in previous_assignments:
                new_assignments.append(assignment)

        if new_assignments:
            recipient_email = "2210030344@klh.edu.in"
            subject = "New KLH Assignment Alert A4"
            message = ''
            for assignment in new_assignments:
                message += f"New Assignment of {assignment['subject']}. Must be submitted by {assignment['date']}. Click on the link to submit the assignment {assignment['url']} \n"
            print(message)
            send_email(recipient_email,subject,message)
            # Update the stored assignments
            updated_assignments = previous_assignments + new_assignments
            save_assignments(updated_assignments)
    except Exception as e:
        logging.error("Error occurred while retrieving assignments: %s", str(e))


if __name__ == "__main__":
    main()
