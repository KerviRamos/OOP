"""Tesla Sales Classes"""

#!usr/bin/env python3
# -*- coding: UTF-8 -*-


class OaklandDealership:
    """Car Dealership Class Located in Oakland, CA"""

    inventory = {}

    @classmethod
    def update(cls, obj: "TeslaVehicle") -> None:
        """Appends newly created cars to the dealership inventory catalog - Side Effect Function"""
        if obj.model in cls.inventory:
            cls.inventory[obj.model] += 1
        else:
            cls.inventory[obj.model] = 1

    @classmethod
    def count_all_vehicles(cls) -> str:
        """Retrieve all total vehicle counts"""
        return TeslaVehicle.num_vehicles


class TeslaVehicle:
    """Tesla Vehicle Class"""

    num_vehicles: int = 0

    def __new__(cls, *args, **kwargs) -> "TeslaVehicle":
        """Object Creation"""
        return super().__new__(cls)

    def __init__(self, color: str, model: str) -> None:
        """Initializing Obj"""
        self.__color: str = color
        self.model: str = model
        self.__class__.num_vehicles += 1
        OaklandDealership.update(self)

    def __repr__(self) -> str:
        """Object Representation"""
        return f"{type(self).__name__} ({id(self)}): {self.model}, {self.__color}"


def main() -> None:
    """Testing Function"""
    # Simple Test
    cars = [
        TeslaVehicle("red", "Model X"),
        TeslaVehicle("red", "Model X"),
        TeslaVehicle("red", "Model Y"),
        TeslaVehicle("red", "Model 3"),
        TeslaVehicle("red", "Model X"),
    ]
    print("Created Car Instances", *cars, sep="\n")
    print(
        "Dealership Inventory",
        OaklandDealership.count_all_vehicles(),
        OaklandDealership.inventory,
        sep="\n",
    )


if __name__ == "__main__":
    main()
