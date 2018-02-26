#coding: utf-8

###########################################
##								  		 ##
##								  		 ##
## Script para enviar correo electrónico ##
##				Carlos García			 ##
##										 ##
##	   								     ##
###########################################

import smtplib
import getpass
#Librerias necesarias para construir el mensaje correctamente
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print'''
╔╗─╔╦═══╦╗──╔╗──╔═══╗╔╗
║║─║║╔══╣║──║║──║╔═╗║║║
║╚═╝║╚══╣║──║║──║║─║║║║
║╔═╗║╔══╣║─╔╣║─╔╣║─║║╚╝
║║─║║╚══╣╚═╝║╚═╝║╚═╝║╔╗
╚╝─╚╩═══╩═══╩═══╩═══╝╚╝
'''

print 'BIENVENIDO AL PROGRAMA DE CORREO AUTOMÁTICO DE CARLOS\n'

src = raw_input('Escriba su correo electronico\n')
pwd = getpass.getpass('Escriba su contraseña\n')
dst = raw_input('Escriba la dirección de destino\n')
sub = raw_input('Escriba una cabecera para el correo\n')
msg = raw_input('Escriba el mensaje\n')

email = MIMEMultipart()
#Construcción del header del mensaje
email['From'] = src; email2['To']=dst; email2['Subject']=sub
#Texto del mensaje
email.attach(MIMEText(msg))

try:
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	print '>>>>>>>>>>> Servidor iniciado <<<<<<<<<<<<<'
	try:
		server.login(src,pwd)
		try:
			ans = raw_input('¿Quiere confirmar el envío?(s/n)\n')
			if ans.lower() == 's':
				server.sendmail(src,dst,email.as_string())			
				print '>>>>>>>>>>> Correo enviado a',dst,'<<<<<<<<<<<<'
			else:
				print '>>>>>>>>>>> Envío de correo cancelado <<<<<<<<<<<<<'
				server.quit()
				exit(0)
		except:
			print('Error al enviar el correo electronico')
	except:	
		print('Error al iniciar sesion en Gmail')
	server.quit()
except:
	print('Error al iniciar el servidor SMTP')