#-------------------------------------------------------------------------------
# Name:         send_sms.py
# Purpose:      This Python script allows the user to send SMS via their 
#               Twilio SMS Gateway.
# Author:       Kiran Chandrashekhar
# Created:      18-Dec-2022
#-------------------------------------------------------------------------------

import re
from twilio.rest import Client

import conf

class SendSMS:
    def __init__(self):
        self.account_sid   = conf.ACCOUNT_SID
        self.auth_token   = conf.AUTH_TOKEN
        self.from_number  = conf.FROM_NUMBER
     
    #---------------------------------------------------------------
    #   Sanitize Mobile Number
    #---------------------------------------------------------------
    def sanitize_mobile_number(self, mobile):
        mobile1 = None
        try:          
            mobile1 = re.sub('\D', '', mobile)            
            mobile1 = f'+{mobile1}'
        except Exception as e:
            print(str(e))        
        return mobile1

    #---------------------------------------------------------------
    #   Send SMS using Twilio 
    #---------------------------------------------------------------
    def send_sms_message(self, message, to_number):
        
        ret = {}
        ret['success'] = False
        try:     
            client = Client(self.account_sid, self.auth_token)
            
            param = {}
            param['to']   = self.sanitize_mobile_number(to_number)
            param['from_'] = self.from_number
            param['body'] = message

            response = client.messages.create(**param)

            if hasattr(response, 'sid'):
                ret['success'] = True          
                ret['sid'] = response.sid          
      
        except Exception as e:
            print(str(e))

        return ret

def main():
    
    otp_code = 123456
    message = f"Your verification code for login is: {otp_code}"
    
    to_number = '917829713845'
    obj = SendSMS()
    ret = obj.send_sms_message(message, to_number)
    
if __name__ == '__main__':
    main()
    print("Done")