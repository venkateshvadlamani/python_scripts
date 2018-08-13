import smtplib



"""Send Gmail 

This is 
"""
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('currency@gmail.com',  'Pehava8pandu&me')
smtpObj.sendmail('currency@gmail.com', 'currency@gmail.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()