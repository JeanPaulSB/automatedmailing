import pandas as pd
import logging
import smtplib
import ssl
import os
import csv

from dotenv import load_dotenv
from email.message import EmailMessage
from exceptions import alreadySent

# setting up the logger
logging.basicConfig(format='%(asctime)s %(message)s',filename = "logger.log",level = logging.DEBUG)


load_dotenv()
# google sheet id and current worskheetname 
googleSheetId = '1wuHLUD9QZNnf8STTkXylxxDCc0czEYjhoVfIVCwTv5Y'
worksheetName = 'Form'
URL = f'https://docs.google.com/spreadsheets/d/{googleSheetId}/gviz/tq?tqx=out:csv&sheet={worksheetName}'

# getting sheet as csv and then reading it as a dataframe
df = pd.read_csv(URL)




email_sender = "botdomus@gmail.com"
# reading password from .env file
email_password = os.getenv('password')
email_recievers = ["jeanpaulsierraboom@gmail.com"]

subject =  "TRACKING"


body = f"""
<html>

<body style="margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; flex-direction: column;">
  
<div class="container" style="width: 75%; height: 100vh; display: flex; flex-direction: column; background-color: #18097a; justify-content: center; align-items: center; color: white; font-family: Arial; font-weight: 700;">
  <p>Hola Pedro!</p>
  <p>Hablemos de las casualidades, de la suerte o de la vida. De todo lo que nos<br>tuvo que enseññar, todo lo que tuvimos que vivir,aprender, y cuántas cosas <br>
tuviste que pasar para tomar la decisión en este preciso momento de tu vida de <br>
 compartir cada momento con mis cuatro patas caminando a tu lado.
  </p>
  
  <p>
    Y cuánto tuve que esperar yo, jugando muchos días, aprendiendo lo que debía <br> para preparme a tu llegada, todo lo que viví para que la vida me pusiera en tu<br>camino,desde el segundo en el que pensaste si era yo esa compañía ideal para<br> ti. Ese segundo en el que pensaste que podríamos ser mejores amigos por<br>siempre, que me diste una familia y un lugar como tu hijo.
  </p>
  <p>
    No te conozco aún pero mis cuidadores ya me hablaron de ti, ellos me aman<br> demsiado, me cuidan mucho y aunque les da nostalgia que me vaya, ¡están <br> felices por tus ganas de verme! Ya me dijeron como piensas llamarme, donde <br> voy a vivir y lo importante que soy para ti. Por eso soy muy juicioso y me como<br>toda la comida, aprendor a ir al baño aunque a veces me equivoco, pero lo estoy<br>intentado. Me falta mucho por apprender pero quiero aprender a tu lado... Hay<br>muchas cosas que no conocemos del otro pero llegamos hasta aquí, y seré el<br>reflejo de tu respesto, tu amor, tu paciencia, tu bondad, tu comprensión y tu<br>compromiso.
  </p>
  <p>
    Quiero jugar, que me dediques tiempo cada día, sé que estás ocupado pero<br>quiero pasar tiempo de calidad contigo, ojalá me lleves a tus viajes.<br>
 también quiero conocer como tú, me gusta ensuciarme, así que llévame a ser lo<br> que soy, un ser que disfruta de la naturaleza, de la compañía y del amor, no<br>
    sólo me sirvas la comida y me ignores en casa, ten en cuenta que mi presencia<br>en tu vida no será eterna. Pero siempore recuerda que tú serás lo que yo más<br>ame en el mundo, y espero que el lugar que me des en tu corazón sea lo<br>
    suficientemente grande para que yo pueda mover mucho mi colita y nuestras<br> almas siempre estén conectadas, en todo momento y con el paso del tiempo.
  </p>
</div>
</body>
</html>

"""

# getting selected users
pendingUsers = df[df['Enviar'] == 1]

context = ssl.create_default_context()

for index,row in pendingUsers.iterrows():
    name = row['Nombre']
    petName = row['Nombre del Cachorro']
    email = row['Correo Electrónico']
    trackID = row['Guía']


    # duplicated status
    duplicated = False
    # reading db
    with open('db.txt','r') as f:
        lines = list(map(lambda x: x.replace('\n',''),f.readlines()))
        try:
            if email in lines:
                raise alreadySent
                print("duplicated hmmm")
        except alreadySent:
            duplicated = True
            logging.error(f"Email already sent to user with email:{email} (skipping email) ")


        
    if not duplicated:
    # writing into db
        print("about to send email...")



        body = f"""
        <html>
        <body>
        <h1>Hola {name}!</h1>
        <h5>El número de tu guía es {trackID}</h5>
        </body>
        </html>
        
        
        
        
        
        """
        # setting up email
        em = EmailMessage()
        em['From'] = email_password
        em['To'] = email
        em['Subject'] = subject
        em.set_content(body,subtype = 'html')

        # sed
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as smtp:
            try:
                smtp.login(email_sender,email_password)
                smtp.send_message(em)
                logging.info(f"Email sended to: {email} succesfully")
                with open('db.txt','a') as f:
                    print(email,file = f)
            except Exception as e:
                logging.error(str(e))
            #smtp.sendmail(email_sender,email,em.as_string())
        
        







 


"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as smtp:
    try:
        smtp.login(email_sender,email_password)
        smtp.send_message(em)
        logging.info(f"Email sended to: {email_recievers} successfully")
    except Exception as e:
        logging.error(str(e))
    #smtp.sendmail(email_sender, email_recievers, em.as_string())
"""

