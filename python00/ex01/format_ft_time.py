import datetime


current_date = datetime.datetime.now()
delta = (current_date - datetime.datetime(1970, 1, 1))
print(f"Seconds since January 1, 1970: "
      f"{delta.total_seconds():,.4f} or "
      f"{delta.total_seconds():e} in scientific notation")
print(current_date.strftime("%b %d %Y"))
