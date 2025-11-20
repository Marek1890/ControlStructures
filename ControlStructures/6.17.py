t = input("Enter time (hh:mm): ")
h, m = map(int, t.split(":"))
suffix = "am"
if h == 0:
    h = 12
elif h == 12:
    suffix = "pm"
elif h > 12:
    h -= 12
    suffix = "pm"
print(f"{h}:{m:02d}{suffix}")
