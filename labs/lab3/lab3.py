"""
Name: Scarlett Duncan
lab3.py
Problem: Create code using for loops to calculate the average number of vehicles on a road per day, the total vehicles
on all roads, and the average number of vehicles per road.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    total_vehicles = 0

    amt_roads = eval(input("How many roads were surveyed?"))
    for road in range(1, amt_roads+1):
        road_day_total = 0
        print("how many days was road", road, "surveyed?", end=" ")
        amt_days = eval(input(""))
        for day in range(1, amt_days+1):
            print("\tHow many cars traveled on day", day, "?", end="")
            cars = eval(input(""))
            road_day_total = (road_day_total + cars)
            total_vehicles = total_vehicles + cars
            road_day_avg = round(road_day_total/amt_days, 1)
        road_avg = round(total_vehicles/amt_roads, 2)
        print("Road", road, "average vehicles per day:", road_day_avg)
    print("Total number of vehicles traveled on all roads:", total_vehicles)
    print("Average number of vehicles per road:", road_avg)
