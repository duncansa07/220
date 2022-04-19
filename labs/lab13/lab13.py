"""
Name: Scarlett Duncan
lab13.py

Problem: Write code that serves as a capstone to demonstrate overall coding bits learned and to demonstrate list sorting

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    file = open(filename, "r")
    file_str = file.readline()
    list_trades = file_str.split(" ")
    acc = 1
    for i in range(len(list_trades)):
        stocks_traded = eval(list_trades[i])
        if stocks_traded > 830:
            timestamp = acc
            print("Warning: Over 830 stocks traded in 1 second. Time:{} seconds".format(timestamp))
        elif stocks_traded == 500:
            timestamp = acc
            print("Alert: 500 stocks traded in 1 second. Time:{} seconds".format(timestamp))
        acc = acc + 1
    file.close()


