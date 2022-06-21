from datetime import datetime
import time
dt = datetime(2018, 1, 1)
print(datetime.now())
dt2 = datetime.strptime("2032/05/08", "%Y/%m/%d")


dt3 = datetime.fromtimestamp(time.time())
print(dt2)
print(dt3)

print(f"{dt.year}/{dt.month}")

dt.strftime("%y/%m")

print(dt2 < dt3)
