from models import Car

cars = [
    Car("BMW", "640d", 2016, 28000),
    Car("Volkswagen", "Golf 6 2.0 TDI", 2011, 9500),
    Car("Audi", "A6 3.0 TDI", 2015, 18000),
    Car("Mercedes", "CLS 350 CDI", 2014, 22000)
]

print("=== АВТОСАЛОН ===")

for car in cars:
    print(car.show_info())

print("\n=== КОЛИ НАД 20000 ЕВРО ===")

for car in cars:
    if car.is_expensive():
        print(car.show_info())

print("\n=== СОРТИРАНЕ ПО ЦЕНА ===")

cars.sort(key=lambda car: car.price)

for car in cars:
    print(car.show_info())

print("\n=== ОТСТЪПКА ЗА BMW 640d ===")

cars[0].apply_discount(10)

print(cars[0].show_info())