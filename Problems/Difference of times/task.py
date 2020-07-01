# put your python code here
hours1 = int(input())
minutes1 = int(input())
second1 = int(input())
hours2 = int(input())
minutes2 = int(input())
second2 = int(input())
difference_times = (hours2 * 60 * 60 + minutes2 * 60 + second2) - (hours1 * 60 * 60 + minutes1 * 60 + second1)
print(difference_times)