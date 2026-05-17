from clas import *
boats = [
    SeaBoat("Catcher", 4, 150.0, 500.0, 2015),
    SeaBoat("Explorer", 12, 300.0, 1200.0, 2020),
    SeaBoat("Wave", 6, 200.0, 800.0, 2015),
    SeaBoat("Titan", 50, 1000.0, 5000.0, 2010),
    SeaBoat("Gull", 2, 50.0, 150.0, 2022)
]

boats.sort(key=lambda x: (x.build_year, -x.engine_power))

print("Відсортований масив:")
for boat in boats:
    print(boat)

target_boat = SeaBoat("Wave", 6, 200.0, 800.0, 2015)

if target_boat in boats:
    index = boats.index(target_boat)
    print(f"\nОб'єкт {target_boat.name} знайдено під індексом {index}.")
else:
    print(f"\nОб'єкт {target_boat.name} не знайдено.")