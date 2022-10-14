from datetime import datetime
import pandas
import random
import smtplib

now = datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

letters = ("letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt")

my_gmail = "necodetesting@gmail.com"
gmail_pw = "apfbufdletsvbwtc"

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    birthday_name = birthday_person["name"]
    chosen_letter = random.choice(letters)

    # read the starting letter
    with open(chosen_letter) as starting_letter:
        contents = starting_letter.read()
        contents = contents.replace("[NAME]", birthday_name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=gmail_pw)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs="necodetesting@yahoo.com",
                msg=f"Subject:Go Look Up\n\nGo Look Up")
