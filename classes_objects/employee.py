""" Employee Class Definition """
#!usr/bin/env python3
# -*- coding: UTF-8 -*-


class Employee:
    """Class Members
    Attributes:
    - first_name, last_name, email, salary
    Methods:
    - retrieve_info()

    Notes: The design does not considered
     - Data validation
     - Encapsulation
    """

    def __new__(cls, *args, **kwargs) -> "Employee":
        """Constructor Phase 1: Employee Object creation"""
        return super().__new__(cls)

    def __init__(
        self, first_name: str, last_name: str, email: str, salary: float
    ) -> None:
        """Contrustor Phase 2: Employee Object initializing state/properties"""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.salary: float = salary

    def __repr__(self) -> str:
        """Employee Object representation"""
        return (
            f"{type(self).__name__} "
            f"state:{(self.first_name, self.last_name, self.email, self.salary)}"
        )

    def retrieve_info(self) -> str:
        """Retrieves the Object state"""
        return (
            f"Name:{self.first_name + " " + self.last_name} "
            f"Email:{self.email} "
            f"Salary:${self.salary:,.1f}"
        )


def main() -> None:
    """Driver testing function"""
    to_print = "Object instantiation"
    data = ["Kervi", "Ramos", "kr@me.com", 90000]
    obj_repr = Employee(*data)
    obj_retrieve = obj_repr.retrieve_info()

    print(to_print, obj_repr, obj_retrieve, sep="\n")


if __name__ == "__main__":
    main()
