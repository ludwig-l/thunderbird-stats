"""
Simple example for demonstrating functionalities
"""

from thunderbirdstats import ThunderbirdStats as ts

# definitions
path = "/home/ludwig/.thunderbird/bdt6qcqz.default/ImapMail/mail.stusta.de/Sent-2"
obj = ts(path)

# call functions
data = obj.get_data_frame()
obj.plot_sent_mails_over_time(data)
