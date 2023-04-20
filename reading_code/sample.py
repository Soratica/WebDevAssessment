import smtplib;
from email.mime.text import MIMEText;
from datetime import date
from datetime import datetime

# This function takes the an email attribute which would be where the email will be going 
# and a message attribute that is a string which would be the content of the email
def foo(email_address,message) :
    msg_from = 'test@webclients.net'
    msg = MIMEText(message.format(first_name = first_name, last_name = last_name))
    msg['Subject'] = 'Important'
    msg['From'] = msg_from
    msg['To'] = email_address

    smtp = smtplib.SMTP('emgw.local:25')
    smtp.sendmail(msg_from,email_address,msg.as_string())
    smtp.quit()

today = date.today()

seen = {}

# Opens and reads a csv file named user_data
# for each record in the csv file, save the email_address, first_name, last_name, birth_date, state_prov
# convert the birthdate to a datetime object
# if statement calls foo() function if age of user of current record is greater than and equal to 18 and also less than 65
# if statement also has the condition that the email address of the user hasn't been sent an email
# using record data send email to email address with message that contains user first and last name
# email_addresses get logged in 'seen' hash with value of 1
with open("user_data.csv","r") as fh:
    for ln in fh:
        email_address, first_name, last_name, birth_date, state_prov = ln.strip().split(',')
        birth_date = datetime.strptime(birth_date,"%Y-%m-%d")

        # To skip users that live in California or New York
        # switch state_prov
        #     case 'CA':
        #        continue
        #     case 'NY':
        #        continue
        #     case _:
        #        break

        # Issue with this is that the month and day is not accounted for and doesn't account for Feb 29th babies
        age = today.year - birth_date.year # - ((today.month, today.day) < (birth_date.month, birth_date.day))  <-- could be fixed with this

        if ((age >= 18) and (age < 65) and (not seen.has_key(email_address))) :
          foo(email_address,"Dear {first_name} {last_name}, Hello!\n"
            .format(first_name = first_name, last_name = last_name))
          seen[email_address] = 1

