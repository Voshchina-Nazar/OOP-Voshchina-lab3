class SeaBoat:
    def __init__(self, name: str, passenger_capacity: int, engine_power: float, cargo_capacity: float, build_year: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Назва човна має бути непорожнім рядком.")

        if type(passenger_capacity) is not int or passenger_capacity < 0:
            raise ValueError("Місткість пасажирів має бути цілим невід'ємним числом.")

        if not isinstance(engine_power, (int, float)) or engine_power <= 0:
            raise ValueError("Потужність двигуна має бути числом більшим за нуль.")

        if not isinstance(cargo_capacity, (int, float)) or cargo_capacity < 0:
            raise ValueError("Вантажопідйомність має бути невід'ємним числом.")

        if type(build_year) is not int or build_year < 1800 or build_year > 2026:
            raise ValueError(f"Рік виробництва має бути цілим числом від 1800 до {2026}.")
        self.name = name
        self.passenger_capacity = passenger_capacity   #
        self.engine_power = engine_power
        self.cargo_capacity = cargo_capacity
        self.build_year = build_year

    def __eq__(self, other):
        if not isinstance(other, SeaBoat):
            return False
        return (self.name == other.name and
                self.passenger_capacity == other.passenger_capacity and
                self.engine_power == other.engine_power and
                self.cargo_capacity == other.cargo_capacity and
                self.build_year == other.build_year)

    def __repr__(self):
        return f"[{self.name}: рік={self.build_year}, потужність={self.engine_power} к.с., пасажири={self.passenger_capacity}]"

