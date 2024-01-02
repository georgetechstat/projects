import random
import csv

regions = ["North", "East", "West", "South"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Sep", "Oct", "Nov", "Dec"]
car_brands = [
    "Ford",
    "Honda",
    "Toyota",
    "Chevy",
    "Mercedes",
    "Porsche",
    "BMW"
]
car_price = [
    14000,
    6000,
    7500,
    3200,
    18000,
    50000,
    24000
]

car_market_price = list(zip(
    car_brands, list(map(lambda n: n + random.randint(1000, 2500), car_price))
))

with open("car_data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Region", "Month", "Car Brand", "Market Price"])
    for car in car_market_price:
        writer.writerow((random.choice(regions), random.choice(months), *car))
