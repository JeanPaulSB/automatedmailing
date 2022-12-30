import pandas as pd
import logging
import smtplib
import ssl
import os

from dotenv import load_dotenv
from email.message import EmailMessage

# setting up the logger
logging.basicConfig(format='%(asctime)s %(message)s',filename = "logger.log",level = logging.DEBUG)


load_dotenv()
# google sheet id and current worskheetname 
googleSheetId = '1wuHLUD9QZNnf8STTkXylxxDCc0czEYjhoVfIVCwTv5Y'
worksheetName = 'Form'
URL = f'https://docs.google.com/spreadsheets/d/{googleSheetId}/gviz/tq?tqx=out:csv&sheet={worksheetName}'

# getting sheet as csv and then reading it as a dataframe
df = pd.read_csv(URL)

print(df['Dirección de correo electrónico'])


email_sender = "botdomus@gmail.com"
# reading password from .env file
email_password = os.getenv('password')
email_recievers = ["jeanpaulsierraboom@gmail.com"]

subject =  "Prueba"


body = f"""
<html>
<body>
<div style = "background-color:blue;">
    <h1>Just testing</h1>
    <p style = "color:#white; padding:10px;">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ornare ex nisi, ac condimentum ligula cursus vitae.<br>
        Nam tristique massa sed venenatis facilisis. Pellentesque eu elit ligula. Fusce ultrices enim vel vulputate blandit. <br>
        Suspendisse tincidunt enim eu felis rutrum dictum. Sed commodo elementum aliquet. Donec nec finibus felis.
    
    </p>
</div>
</body>
</html>

"""



em = EmailMessage()
em['From'] = email_password
em['To'] = email_recievers
em['Subject'] = subject
em.set_content(body,subtype = 'html')


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as smtp:
    try:
        smtp.login(email_sender,email_password)
        smtp.send_message(em)
        logging.info(f"Email sended to: {email_recievers} successfully")
    except Exception as e:
        logging.error(str(e))
    #smtp.sendmail(email_sender, email_recievers, em.as_string())
