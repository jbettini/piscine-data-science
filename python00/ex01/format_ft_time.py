import datetime


current_date = datetime.datetime.now()
delta = (current_date - datetime.datetime(1970, 1, 1))

print(f"Seconds since January 1, 1970: {delta.total_seconds():,.4f} or {delta.total_seconds():n}  in scientific notation")
print(current_date.strftime("%B %d %Y"))