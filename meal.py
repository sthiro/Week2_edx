# Breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
# Prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time
# If it’s not time for a meal, don’t output anything at all.

# Eg : 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

#time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).


#Challenge 12 H format

#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.

#_________________________________
# Task 1  (Done)     |    Task 2  
#---------------------------------
# 24H format         | 12H format   
#_________________________________

#******************************************************************************************

time_24 = input("What time is it? ")


def main():
    time_integer = convert(time_24)

    if 7 <= time_integer <= 8:
        print("breakfast time")
    
    elif 12 <= time_integer <= 13:
        print("lunch time")

    elif 18 <= time_integer <= 19:
        print("dinner time")

    


def convert(time):
    hours, minutes = time.split(":") 
    hours, minutes = int(hours), int(minutes)/60 # Hours and minute are interger now 

    return hours + minutes # if time = "7:30" convert and returns 7.5


if __name__ == "__main__":
    main()



