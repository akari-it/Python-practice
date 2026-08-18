def rank(point):
    if point >= 90:
        return "S"
    elif point >= 70:
        return "A"
    elif point >= 50:
        return "B"
    elif point >= 30:
        return "C"
    else:
        return "D"

print(rank(59))