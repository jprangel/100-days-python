import pandas
from datetime import datetime
import random
import smtplib

path_letter = "letter_templates"
project_folder = "32day-AutomatedBirthdayWisher"
birthday_file = f"{project_folder}/birthdays.csv"
my_email = "contact@gmail.com"
password = "12345"
mail_server_addr = "smtp.gmail.com"

birthday_csv = pandas.read_csv(birthday_file)

today = datetime.now()
today_tuple = (today.month, today.day)

birthday_dict = { (birthday_row['month'], birthday_row['day']): birthday_row for (index, birthday_row) in birthday_csv.iterrows() }

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"{project_folder}/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person['name'])
        
    with smtplib.SMTP(mail_server_addr) as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(my_email, 
                      birthday_person['email'], 
                      msg=f"Subject:Happy Bithday!\n\n{content}")
        
    
    
    
    





