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


style = """  <style type="text/css">
      @media only screen and (min-width: 620px) {
  .u-row {
    width: 600px !important;
    color-scheme: light only;
  }
  .u-row .u-col {
    vertical-align: top;
    color-scheme: light only;
  }

  .u-row .u-col-33p33 {
    width: 199.98px !important;
    color-scheme: light only;
  }

  .u-row .u-col-66p67 {
    width: 400.02px !important;
    color-scheme: light only;
  }

  .u-row .u-col-100 {
    width: 600px !important;
    color-scheme: light only;
  }

}

@media (max-width: 620px) {
  .u-row-container {
    max-width: 100% !important;
    padding-left: 0px !important;
    padding-right: 0px !important;
    color-scheme: light only;
  }
  .u-row .u-col {
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important;
    color-scheme: light only;
  }
  .u-row {
    width: 100% !important;
    color-scheme: light only;
  }
  .u-col {
    width: 100% !important;
    color-scheme: light only;
  }
  .u-col > div {
    margin: 0 auto;
    color-scheme: light only;
  }
}
body {
  margin: 0;
  padding: 0;
  color-scheme: light only;
}

table,
tr,
td {
  vertical-align: top;
  border-collapse: collapse;
  color-scheme: light only;
}

p {
  margin: 0;
  color-scheme: light only;
}

.ie-container table,
.mso-container table {
  table-layout: fixed;
  color-scheme: light only;
}

* {
  line-height: inherit;
  color-scheme: light only;
}

a[x-apple-data-detectors='true'] {
  color: inherit !important;
  text-decoration: none !important;
  color-scheme: light only;
}

table, td { color: #000000;color-scheme: light only; } #u_body a { color: #0000ee; text-decoration: underline; color-scheme: light only;} @media (max-width: 480px) { #u_row_1 .v-row-background-color { background-color: #236fa1 !important; color-scheme: light only;} #u_row_1.v-row-background-color { background-color: #236fa1 !important; color-scheme: light only;} #u_row_1 .v-row-columns-background-color-background-color { background-color: #235070 !important; color-scheme: light only;} #u_column_1 .v-col-padding { padding: 50px 0px 0px !important;color-scheme: light only; } #u_column_1 .v-col-border { border-top: 0px solid transparent !important;border-left: 0px solid transparent !important;border-right: 0px solid transparent !important;border-bottom: 0px solid transparent !important; color-scheme: light only; } #u_row_2 .v-row-background-color { background-color: #041c1e !important; color-scheme: light only; } #u_row_2.v-row-background-color { background-color: #041c1e !important; color-scheme: light only; } #u_column_2 .v-col-padding { padding: 50px !important;color-scheme: light only; } #u_column_2 .v-col-border { border-top: 0px solid transparent !important;border-left: 0px solid transparent !important;border-right: 0px solid transparent !important;border-bottom: 0px solid transparent !important; color-scheme: light only; } #u_content_text_18 .v-container-padding-padding { padding: 14px !important; color-scheme: light only; } #u_content_text_18 .v-color { color: #ffffff !important; color-scheme: light only; } #u_content_text_18 .v-line-height { line-height: 140% !important; color-scheme: light only; } #u_content_image_23 .v-container-padding-padding { padding: 6px !important; color-scheme: light only; } #u_content_text_23 .v-container-padding-padding { padding: 40px !important; color-scheme: light only; } #u_content_text_23 .v-text-align { text-align: center !important; color-scheme: light only; } #u_content_text_23 .v-line-height { line-height: 170% !important; color-scheme: light only; } }
    </style>
  
  
  
  
"""

body = """
<html>
<head>
  <!--[if gte mso 9]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="only">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!-->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<![endif]-->
  <title></title>
  <style></style>
  </head>

<body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #e7e7e7;color: #000000">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #e7e7e7;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #e7e7e7;"><![endif]-->
    

<div id="u_row_1" class="u-row-container v-row-background-color" style="padding: 0px;background-color: #ffffff">
  <div class="u-row v-row-columns-background-color-background-color" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #041c1e;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: #ffffff;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr class="v-row-columns-background-color-background-color" style="background-color: #041c1e;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" class="v-col-padding v-col-border" style="background-color: #041c1e;width: 600px;padding: 70px 0px 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div id="u_column_1" class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="background-color: #041c1e;height: 100%;width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div class="v-col-padding v-col-border" style="height: 100%; padding: 70px 0px 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px;font-family:'Montserrat',sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
      
      <img align="center" border="0" src="https://assets.unlayer.com/projects/127139/1673052727874-289756.jpg" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 489px;" width="489"/>
      
    </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>



<div id="u_row_2" class="u-row-container v-row-background-color" style="padding: 0px;background-color: #ffffff">
  <div class="u-row v-row-columns-background-color-background-color" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: #ffffff;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr class="v-row-columns-background-color-background-color" style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" class="v-col-padding v-col-border" style="background-color: #041c1e;width: 600px;padding: 50px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
<div id="u_column_2" class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="background-color: #041c1e;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
  <!--[if (!mso)&(!IE)]><!--><div class="v-col-padding v-col-border" style="height: 100%; padding: 50px 0px 20px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
  
<table id="u_content_text_18" style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:0px 40px;font-family:'Montserrat',sans-serif;" align="left">
        
  <div class="v-color v-text-align v-line-height" style="color: #ffffff; line-height: 170%; text-align: left; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">Hablemos de las casualidades, de la suerte o de la vida. De todo lo que nos tuvo que ense??ar, todo lo que tuvimos que vivir, aprender, y cu??ntas cosas tuviste que pasar para tomar la decisi??n en este preciso momento de tu vida de compartir cada momento con mis cuatro patas caminando a tu lado.</span></p>
<p style="font-size: 14px; line-height: 140%;">??</p>
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">Y cu??nto tuve que esperar yo jugando muchos d??as, aprendiendo lo que deb??a para prepararme a tu llegada, todo lo que viv?? para que la vida me pusiera en tu camino, desde el?? segundo en el que pensaste si era yo esa compa????a ideal para ti. Ese segundo en el que pensaste que podr??amos ser mejores amigos por siempre, que me diste una familia y un lugar como tu hijo.</span></p>
<p style="font-size: 14px; line-height: 140%;">??</p>
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">No te conozco a??n pero mis cuidadores ya me hablaron de ti, ellos me aman demasiado, me cuidan mucho y aunque les da nostalgia que me vaya, ??est??n?? felices por tus ganas de verme! Ya me dijeron como piensas llamarme, donde?? voy a vivir y lo importante que soy para ti. Por eso soy muy juicioso y me como toda la comida, aprendo a ir al ba??o aunque a veces me equivoco, pero lo estoy intentando. Me falta mucho por aprender pero quiero aprender a tu lado... Hay muchas cosas que no conocemos del otro pero llegamos hasta aqu??, y ser?? el reflejo de tu respeto, tu amor, tu paciencia, tu bondad, tu comprensi??n y tu compromiso.</span></p>
<p style="font-size: 14px; line-height: 140%;">??</p>
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">Quiero jugar, que me dediques tiempo cada d??a, s?? que est??s ocupado pero quiero pasar tiempo de calidad contigo, ojal?? me lleves a tus viajes.</span><br /><span style="font-size: 12px; line-height: 16.8px;">tambi??n quiero conocer como t??, me gusta ensuciarme, as?? que ll??vame a ser lo que soy, un ser que disfruta de la naturaleza, de la compa????a y del amor, no</span><br /><span style="font-size: 12px; line-height: 16.8px;">s??lo me sirvas la comida y me ignores en casa, ten en cuenta que mi presencia en tu vida no ser?? eterna. Pero siempre recuerda que t?? ser??s lo que yo m??s ame en el mundo, y espero que el lugar que me des en tu coraz??n sea lo suficientemente grande para que yo pueda mover mucho mi colita y nuestras almas siempre est??n conectadas, en todo momento y con el paso del tiempo.</span></p>
<p style="font-size: 14px; line-height: 140%;">??</p>
<p style="font-size: 14px; line-height: 140%;">??</p>
<p style="font-size: 14px; line-height: 140%;">??</p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>



<div class="u-row-container v-row-background-color" style="padding: 0px;background-color: #ffffff">
  <div class="u-row v-row-columns-background-color-background-color" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
    <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="v-row-background-color" style="padding: 0px;background-color: #ffffff;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr class="v-row-columns-background-color-background-color" style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="200" class="v-col-padding v-col-border" style="background-color: #041c1e;width: 200px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
<div class="u-col u-col-33p33" style="max-width: 320px;min-width: 200px;display: table-cell;vertical-align: top;">
  <div style="background-color: #041c1e;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
  <!--[if (!mso)&(!IE)]><!--><div class="v-col-padding v-col-border" style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
  
<table id="u_content_image_23" style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Montserrat',sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="center">
      
      <img align="center" border="0" src="https://assets.unlayer.com/projects/127139/1673054344717-pngwing.com%20(3).png" alt="" title="" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 180px;" width="180"/>
      
    </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
<!--[if (mso)|(IE)]><td align="center" width="400" class="v-col-padding v-col-border" style="background-color: #041c1e;width: 400px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;" valign="top"><![endif]-->
<div class="u-col u-col-66p67" style="max-width: 320px;min-width: 400px;display: table-cell;vertical-align: top;">
  <div style="background-color: #041c1e;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
  <!--[if (!mso)&(!IE)]><!--><div class="v-col-padding v-col-border" style="height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;"><!--<![endif]-->
  
<table id="u_content_text_23" style="font-family:'Montserrat',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td class="v-container-padding-padding" style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Montserrat',sans-serif;" align="left">
        
  <div class="v-color v-text-align v-line-height" style="color: #ffffff; line-height: 210%; text-align: left; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 170%;"><span style="font-size: 12px; line-height: 20.4px;">??Recuerda que con el siguiente c??digo podr??s estar actualiz??ndote entrando a nuestra p??gina web y tendr??s a tu alcance mi informaci??n, mis vacunas, mis fotos y la fecha pr??xima de cu??ndo podremos vernos!</span></p>
<p style="font-size: 14px; line-height: 170%;">??</p>
<p style="font-size: 14px; line-height: 170%;"><strong><span style="font-size: 12px; line-height: 20.4px;">C??digo:{0}??</span></strong></p>
<p style="line-height: 170%; font-size: 14px;"><span style="color: #ecf0f1; font-size: 14px; line-height: 23.8px;"><a rel="noopener" href="https://www.somosdomus.com/track-your-order/" target="_blank" style="color: #ecf0f1;"><span style="font-size: 14px; line-height: 23.8px;"><span style="font-size: 10px; background-color: #000000; line-height: 17px;"><strong>Click aqu?? para ir a la p??gina</strong></span></span></a></span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>


    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>
  <!--[if mso]></div><![endif]-->
  <!--[if IE]></div><![endif]-->
</body>
</html>


"""





# getting selected users
pendingUsers = df[df['Enviar'] == 1]

context = ssl.create_default_context()

for index,row in pendingUsers.iterrows():
    name = row['Nombre Propietario']
    petName = row['Nombre del Cachorro']
    email = row['Correo Electr??nico']
    trackID = row['Gu??a']


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

        body = body.format(int(trackID))
        body = body.replace('<style></style>', style)

        
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

