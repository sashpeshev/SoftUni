from datetime import datetime, timedelta
date = datetime.strptime(input(), "%d-%m-%Y")
date_after_1000_days = date + timedelta(days=1000)
print(date_after_1000_days.strftime("%d-%m-%Y"))
