#Import the required libraries(Modules)
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

#Initialize connection to our Email Server. We will use Gmail here
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

# Login with your Email and Password
smtp.login('EMAIL ADDRESS', 'PASSWORD')

#Send our email message 'Automated Test Mail'
def message(subject="Test Mail",
			text="This is the Automated Test Mail.", img=None,
			attachment=None):
	
	#Build message contents
	msg = MIMEMultipart()
	
	#Add Subject
	msg['Subject'] = subject
	
	#Add Text
	msg.attach(MIMEText(text))

#Write the receivers Email Address
to = ["EMAIL ADDRESS OF RECEIVER"]

#SendMail Function
smtp.sendmail(from_addr="EMAIL ADDRESS OF SENDER",
			to_addrs=to, msg=msg.as_string())

#Close the Connection
smtp.quit()
