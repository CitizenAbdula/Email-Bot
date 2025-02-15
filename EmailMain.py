# import Simple Mail Transfer Protocol Library to send emails 
import smtplib
# import Operating System Library to get the environment variable
import os
# import Speech Recognition Library to recognize speech
import speech_recognition as sr
# import Pyttsx3 Library to convert text to speech
import pyttsx3
# import EmailMessage Library to send emails
from email.message import EmailMessage
# import dotenv Library to get the environment variable
from dotenv import load_dotenv

# initialize the recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()
# load the environment variable from the .env file
load_dotenv()
# get the environment variable from the .env file
my_password = os.environ.get('MY_SECRET_PASSWORD')

# function to convert text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
# try to record the audio
    try:
        # use the microphone as the source for input
        with sr.Microphone() as source:
            print("Listening...")
            # listen for user input
            voice = listener.listen(source)
            # use Google to recognize audio
            info = listener.recognize_google(voice)
            # print the user input
            print(info)
            return info.lower()
        

    # if there is an error, pass
    except:
        pass


def send_email(receiver, subject, message):
    # Connecting to the server with the SMTP server and port number
    server = smtplib.SMTP('Smtp.gmail.com', 587)
    # Start Trsut Layer Security encryption to secure the connection 
    server.starttls()
    # Login to the server with email and password
    server.login('your_email, my_password)
    # Send email to the recipient with the message 
    email = EmailMessage()
    email['From'] = 'Your_email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.sendmail('Your_email', 
                    'Receiver_email', 
                    'Hello, this is a test email.')

email_list = {
    'Name 1': 'Name1@gmail.com',
    'Name 2': 'Name2@gmail.com',
    'Name 3': 'Name3@gmail.com',



}



def get_email_info():
    talk('Who do you want to send the email to?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of the email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey brother, your email has been sent')
    talk('Do you want to send another email?')
    send_more = get_info()
    if 'yes' in send_more:
        print('Sending another email...')
        get_email_info()
    else:
        talk('Thank you for using the email service')
        exit()
        ()

get_email_info()
