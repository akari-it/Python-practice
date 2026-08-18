def discount(price):
    if price >= 1000:
        return price - 500
    else:
        return price - 100

print(discount(1530))
print(discount(300))
