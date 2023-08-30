# Day definer

def dayCounter(Year, months):
    count_months = Year*12 + months
    count_days = 29*count_months
    print("Amount of days=")
    print(count_days)


print("Enter Years")
Year = int(input())
print("Enter Months")
months = int(input())
dayCounter(Year,months)
