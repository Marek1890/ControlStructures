x = float(input("x: "))
y = float(input("y: "))
if x == 0 and y == 0:
    print("Point at origin")
elif x == 0:
    print("Point on Y axis")
elif y == 0:
    print("Point on X axis")
elif x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
else:
    print("Fourth quadrant")
