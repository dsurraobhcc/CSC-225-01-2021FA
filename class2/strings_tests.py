import re

# str.split()

# formatted string literals
today = 'Friday'
month = 'September'
date = '9th'
# print(f"Today is {today}, {month} {date}")

# str find
forecast = 'There will be rain today'
print(forecast.find('rain'))

forecast = 'There will be rains today aaaaaaaaaaaaa'
forecast_clean = forecast.replace('aaaaaaaaaaaaa', '')
#print(forecast_clean)

# find trailing a's
# re.match(pattern, string, flags=0)
m = re.match(r'[a]+', forecast)
#print(m)

m = re.search(r'[a]+', forecast)
#print(m)

# re.sub(pattern, repl, string, count=0, flags=0)¶
forecast_clean = re.sub(r'[a]+$', '', forecast)
print(forecast_clean)