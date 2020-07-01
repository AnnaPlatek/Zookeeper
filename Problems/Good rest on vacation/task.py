# put your python code here
duration_in_days = int(input())
daily_food_cost = int(input())
oneway_flight_cost = int(input())
hotel_night_cost = int(input())

total_cost = duration_in_days * daily_food_cost + oneway_flight_cost * 2 + (duration_in_days - 1) * hotel_night_cost
print(total_cost)