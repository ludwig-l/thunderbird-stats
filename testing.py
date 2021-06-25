import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io


def month_to_number(month_str):
    # create date string using year month and day information

    if month_str == "Jan":
       month_number_as_str = "01"
    if month_str == "Feb":
        month_number_as_str = "02"
    if month_str == "Mar":
        month_number_as_str = "03"
    if month_str == "Apr":
        month_number_as_str = "04"
    if month_str == "May":
        month_number_as_str = "05"
    if month_str == "Jun":
        month_number_as_str = "06"
    if month_str == "Jul":
        month_number_as_str = "07"
    if month_str == "Aug":
        month_number_as_str = "08"
    if month_str == "Sep":
        month_number_as_str = "09"
    if month_str == "Oct":
        month_number_as_str = "10"
    if month_str == "Nov":
        month_number_as_str = "11"
    if month_str == "Dec":
        month_number_as_str = "12"

    return month_number_as_str

def is_date_above(date_1, date_2):
    # check if date_1 is above date_2 (both dates given in yyyy-mm-dd format as str)

    if date_1[0:4] < date_2[0:4]:
        return False
    elif date_1[5:7] < date_2[5:7]:
        return False
    elif date_1[9:11] < date_2[9:11]:
        return False
    else:
        return True

# path to thunderbird 
path = "/home/ludwig/.thunderbird/bdt6qcqz.default/ImapMail/mail.stusta.de/Sent-1"

# read in lines of file beginning with regarded pattern
pattern = "Date: "
with open(path, "r", encoding="latin1") as f:
    timestamps = []
    for ln in f:
        if ln.startswith(pattern):
            timestamps.append(ln[len(pattern):])
f.close()

# create title bar with corresponding names for values of interest
title_row = ["weekday day month year time timezone"]

# create data frame from data from file
timestamps = title_row + timestamps

# create dataframe
df = pd.read_csv(io.StringIO('\n'.join(timestamps)), sep=" ", dtype={5:str}) 

# remove comma after name of weekday 
df["weekday"] = df["weekday"].apply(lambda str: str[:-1])
# df.insert(0, "date", df["year", "month", "day"].apply(create_date_str, axis=0))

# create new column with date in proper format
df.insert(0, "date", "")
df["date"] = (df["year"].astype(str)
             + ["-"] * len(df["date"])
             + df["month"].apply(month_to_number)
             + ["-"] * len(df["date"])
             + df["day"].astype(str).apply(lambda day: day.zfill(2)))

print(df)


# reduce number of entries to plot and analyze
# ...


# plot results
plt.hist(df["date"], bins=650)
plt.ylabel("occurences")
plt.xlabel("dates")
plt.xticks(rotation = 45)
plt.title("Sent emails")
plt.show()

# currently working:
# shows in histogram how many mails were sent on each day (but only the days where mails where sent; empty days are still missing)