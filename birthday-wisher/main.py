
#                            PROJECT DESCRIPTION
#                 ----------------------------------------

# In this project, we create a birthday wisher application. We have a csv file with names, emails and year, month, day of birth
# of our friends and relatives. CSV file [here] ()
# We also have a folder in the present directory. The folder contains 5 templates of birthday wish message, so that we don't get
# to send the same message all the time, or the same message to different people
# Please see template folder [here]

import csv
import datetime as dt
import os
import random
import smtplib

my_email = "anyaray2016@gmail.com"
my_password = "wsoi uzkm tuaw aiqm"

templates = []
directory = 'letter-templates'
for filename in os.listdir(directory):
    template = os.path.join(directory, filename)
    if os.path.isfile(template):                                 # checking if it is a file, and appending it to templates list
        templates.append(template)

random_template = random.choice(templates)

months_list = []
days_list = []
names_list = []
emails_list = []

with open("birthdays.csv") as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
        months_list.append(row['month'])                                     # We create lists (names, emails, month of birth, day of birth) from our dictionary
        days_list.append(row['day'])
        names_list.append(row['name'])
        emails_list.append(row['email'])

new_months = [int(month) for month in months_list]                           # items in months and days lists are strings. We convert to integers
new_days =[int(day) for day in days_list ]                            

new_list = list(zip(names_list, emails_list, new_months, new_days))          # We create a tuple with each item containing name, email, month of birth and day of birth

time_now = dt.datetime.now()

for date in new_list:
    names = [ ]
    emails = [ ]
    celebrants = [ ]
    if date[2] == time_now.month and date[3] == time_now.day:
        celebrants.append(date)
        for people in celebrants:
            name = people[0]
            email = people[1]

            with open(random_template) as content:
                message = content.read()
                addressed_message = message.replace('[NAME]', name)

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=my_password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=email,
                        msg=f"Subject: Happy Birthday\n\n{addressed_message}"
                    )
