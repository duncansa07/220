"""
Name: Scarlett Duncan
lab1.py
Problem: Calculating monthly interest rate from a users annual interest, statement balance, payment, and payment day
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def monthlyinterest():
    annual_interest_rate = eval(input("What is your annual interest rate?"))
    days_in_billing_cycle = eval(input("How many days are in your billing cycle?"))
    previous_balance = eval(input("What was your previous balance?"))
    payment_amount = eval(input("What is your payment amount?"))
    day_of_payment = eval(input("What day of the billing cycle was your payment made?"))
    net_x_days = previous_balance * days_in_billing_cycle
    payment_x_days = payment_amount * (days_in_billing_cycle - day_of_payment)
    net_min_payment = net_x_days - payment_x_days
    avg_daily_balance = net_min_payment / days_in_billing_cycle
    monthly_interest = ((annual_interest_rate/100)/12) * avg_daily_balance
    monthly_int_round = round(monthly_interest, 2)
    print("Your monthly interest is $", monthly_int_round)
monthlyinterest()

