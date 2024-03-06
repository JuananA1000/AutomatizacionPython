import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Abrir el archivo que contiene el contenido del correo
with open('mensaje.txt', 'r') as file:
    contenido_correo = file.read()

# Configurar los detalles del correo
remitente = '___'
contraseña='___'
destinatario = '___'
asunto = 'Asunto del correo'

# Crear un objeto MIMEMultipart para el correo
correo = MIMEMultipart()
correo['From'] = remitente
correo['To'] = destinatario
correo['Subject'] = asunto

# Adjuntar el archivo PDF al correo
archivo_adjunto = MIMEApplication(open('archivo.pdf', 'rb').read(), _subtype='pdf')
archivo_adjunto.add_header('Content-Disposition', 'attachment', filename='archivo.pdf')
correo.attach(archivo_adjunto)

# Agregar el contenido del correo al cuerpo del correo
contenido_correo = MIMEText(contenido_correo)
correo.attach(contenido_correo)

# Configurar el servidor SMTP y enviar el correo
servidor_smtp = smtplib.SMTP('servidor_smtp.ejemplo.com', 587)
servidor_smtp.starttls()
servidor_smtp.login(remitente, contraseña)
servidor_smtp.sendmail(remitente, destinatario, correo.as_string())
servidor_smtp.quit()

# PENDIENTE: Enviar el correo con la posibilidad de introducir tildes en las vocales.
# PENDIENTE: Enviar el correo a varios destinatarios de una sola vez: ¿Con bucles?.
# IDEA: ¿Es posible acceder desde este script a CUALQUIER ruta del equipo? Investigar eso.