'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

#Uncommet to configure in file.
ACCOUNT_SID = "ACc6bc4e62ba004615fe9bbcf9b244d2e8"
AUTH_TOKEN = "600da7b3d7304f152b0525d57b16fd28"
Beans_APP = "AP8305b058325922fcae00f0b8ad1671a5"
Beans_SPAM_ID = "+1 508-401-7549"


#Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
Twil_APP_SID = os.environ['Twil_APP_SID']
Twil_SPAM_ID = os.environ['Twil_SPAM_ID']
