n = int(input())
m = int(input())
t = int(input())

minutes_in_hour = 60
hours_in_day = 24

delivery_minutes = (m + t) % minutes_in_hour
delivery_hours = (n + ((m + t) // minutes_in_hour)) % hours_in_day

print(f'{delivery_hours:02d}:{delivery_minutes:02d}')