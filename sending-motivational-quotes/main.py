#                 DESCRIPTION
#           ------------------------

# In this project, we check whther the day of the week is Wednesday. If yes, we send a
# randon motivational message to a friend from a list of messages in the txt file.
# See quotes.txt [here] (https://github.com/Ray-DevOps/Python-Projects/tree/main/sending-motivational-quotes)


import smtplib
import random
my_email = "anyaray2016@gmail.com"
my_password = "wsoiuzkmtuawaiqm"                

quotes_list = [ ]
with open('quotes.txt') as quotes:
    lines = quotes.readlines()
    for line in lines:
        line = line.strip()                       # line.strip() gets rid of the \n at the end of each line
        quotes_list.append(line)

message = random.choice(quotes_list)

import datetime as dt

time_now = dt.datetime.now()

year = time_now.year
weekday = time_now.weekday()
date_of_birth = dt.datetime(year=1995, month=12, day=25)

if weekday == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="anyaraymond@yahoo.com",
            msg=f"Subject: Happy New Day\n\n{message}"
        )
