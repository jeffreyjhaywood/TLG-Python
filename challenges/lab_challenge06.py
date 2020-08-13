starStr = ""
for row in range(10):
    if row < 5:
        starStr += "*"
    else:
        starStr = starStr[:-1]
    print(starStr)
