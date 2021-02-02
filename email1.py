#sending email
import smtplib

sender = 'source@abc.com'
receivers = ['one@target.com']

message = """From: From Person <source@abc.com>
To: To Person <one@target.com>
Subject: Good Morning

Have a great day.
"""
smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
