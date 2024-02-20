"""Implementing Polymorphism with Employees"""

#!usr/bin/env python3
# -*- coding: UTF-8 -*-


class Employee:
    """Employee Base Class Definition"""

    def __new__(cls, *args, **kwargs) -> "Employee":
        """Employee Object Creation"""
        return super().__new__(cls)

    def __init__(self, first_name: str, last_name: str, hired_date: str) -> None:
        """Employee Object Initializing State - Constructor"""
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._hired_date: str = hired_date

    def __repr__(self) -> str:
        """Object representation"""
        return f"{self._first_name +' '+ self._last_name} Hired date:{self._hired_date}"


class FullTimeEmployee(Employee):
    """FullTimeEmployee extends Employee"""

    def __init__(self, first_name: str, last_name: str, hired_date: str) -> None:
        """Fulltime Object Initializing State - Constructor"""
        super().__init__(first_name, last_name, hired_date)
        self._annual_worked_hrs: float = 2080

    def calculate_salary(self, hourly_rate: float = 80.0) -> float:
        """Annual Salary Calculation"""
        return self._annual_worked_hrs * hourly_rate


class PartTimeEmployee(Employee):
    """PartTimeEmployee extends Employee"""

    _benefit_reduction_rate = 0.80

    def __init__(self, first_name: str, last_name: str, hired_date: str) -> None:
        """Fulltime Object Initializing State - Constructor"""
        super().__init__(first_name, last_name, hired_date)
        self._annual_worked_hrs: float = 1040

    def calculate_salary(self, hourly_rate: float = 60.0) -> float:
        """Annual Salary Calculation"""
        return (
            self._annual_worked_hrs * hourly_rate * type(self)._benefit_reduction_rate
        )


class Contractor(Employee):
    """Contractor extends Employee"""

    def __init__(self, first_name: str, last_name: str, hired_date: str) -> None:
        """Fulltime Object Initializing State - Constructor"""
        super().__init__(first_name, last_name, hired_date)
        self._hourly_rate: float = 63.0

    def calculate_salary(self, total_annual_hrs: int = 2000) -> float:
        """Annual Salary calculation"""
        return self._hourly_rate * total_annual_hrs


def main() -> None:
    """Test Cases"""
    test_cases = [
        FullTimeEmployee("Kervi", "Ram", "2023-04-20"),
        PartTimeEmployee("Sam", "Rolof", "2021-09-03"),
        Contractor("Alex", "Zam", "2020-01-02"),
    ]
    results = map(lambda obj: obj.calculate_salary(), test_cases)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()
