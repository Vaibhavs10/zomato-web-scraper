
# coding: utf-8

import sys
import smtplib
import urllib2
import pandas as pd
from bs4 import BeautifulSoup
from email.mime.text import MIMEText

#First argument = Location
#Second argument = Type of food (Chinese, etc)
#Third argument = Cost for two

url_delivery = "https://www.zomato.com/ncr/"+sys.argv[1]+"-restaurants/"+sys.argv[2]+"?category=1&cft="+sys.argv[3]
page_delivery = urllib2.urlopen(url_delivery)
soup_delivery = BeautifulSoup(page_delivery)
link = soup_delivery.findAll('div', attrs={'class':'card search-snippet-card  search-card '})

details_delivery = []

for item in link:
    rest = item.findAll('a', attrs={'data-result-type':'ResCard_Name'})[0]
    rest_name = rest.text.strip()
    url = rest['href']
    try:
        rating = item.findAll('div',  attrs={'class':'rating-popup'})[0].text.strip()
    except:
        rating = "Rating not available!"
    try:
        phone_no = item.findAll('a', attrs={'class':'item res-snippet-ph-info'})[0]['data-phone-no-str']
    except:
        phone_no = "Number not available!"
    try:
        url_delivery = item.findAll('a', attrs={'data-class_name':'o2_link'})[0]['href']
    except:
        url_delivery = "Restaurant is offline right now!"
    menu = item.findAll('a', attrs={'class':'item result-menu'})[0]['href']
    details_delivery.append({'Name' : rest_name, 'Rating' : rating, 'Phone' : phone_no, 'Delivery_URL' : url_delivery, 'Menu' : menu})

df = pd.DataFrame(details_delivery)
string_to_send = "Hey! here are the places I found:\n"
for i in range(7):
    string_to_send += "Name: " + df.iloc[i]['Name']  + '\n'
    string_to_send += "Rating: " + df.iloc[i]['Rating'] + '\n'
    string_to_send += "Phone Number: " + df.iloc[i]['Phone'] + '\n'
    string_to_send += "Menu: " + df.iloc[i]['Menu'] + '\n'
    string_to_send += "Home Delivery: " + df.iloc[i]['Delivery_URL'] + '\n' + '\n'
    
email_subject = "Your food options are ready!"
email_from = "your_email_id"
email_receivers = ['List of receivers']

def listtostring(lst):
    return ','.join(lst)

def send_email(msg, psd):
    msg_header ="From: " + email_from + "\n" +                 "To: " + listtostring(email_receivers) + "\n" +                 "Subject: " + email_subject + "\n"
    msg_body = msg_header + string_to_send + msg
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(your_email_id, psd)
        smtpObj.sendmail(your_email_id, listtostring(email_receivers), msg_body)
        smtpObj.quit()
    except:
        print "Error: Unable to send email : {err}".format(err=error)

send_email('Regards, \nYour PyScript', your_password)


