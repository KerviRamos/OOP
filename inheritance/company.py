""" Company Object Oriented model - Inheritance"""

#!usr/bin/env python3
# -*- coding: UTF-8 -*-

# Implement descriptor


class Employee:
    """Employee class definition"""

    def __new__(cls, *args, **kwargs) -> "Employee":
        """Object creation"""
        return super().__new__(cls)

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Object initialization"""
        self._firs_name: str = first_name
        self._last_name: str = last_name
        self._email: str = f"{first_name}.{last_name}@me.com"
        self._salary: float = salary

    def fetch_details(self) -> dict[str | str, float]:
        """Summary Info"""
        return (
            self.__dict__
        )  # We need to filter the __dict__ to fetch for the appropiate keys (first_name, last_name, etc)

    def update_details(self, **kwargs) -> None:
        """Update Info"""
        self.__dict__.update(kwargs)


class Developer(Employee):
    """Developer definition"""

    def __new__(cls, *args, **kwargs) -> "Developer":
        """Object creation"""
        return super().__new__(cls)

    def __init__(  # Too many arguments
        self,
        first_name: str,
        last_name: str,
        salary: float,
        technology: str,
        commit_privileges: str = "Admin",
    ) -> None:
        """Object initialization"""
        super().__init__(first_name, last_name, salary)
        self._technology: str = technology
        self._commit_privileges: str = commit_privileges


class Manager(Employee):
    """Manager definition"""

    def __new__(cls, *args, **kwargs) -> "Manager":
        """Object creation"""
        return super().__new__(cls)

    def __init__(
        self,
        first_name: str,
        last_name: str,
        salary: float,
        team_members: set["Employee" | "Developer"],
    ) -> None:
        """Object initialization"""
        super().__init__(first_name, last_name, salary)
        self._developers = team_members
        self._num_of_em = len(team_members)

    def add(self, team_member: "Employee" | "Developer") -> None:
        """Add a new developer - Side Effect"""
        if (
            not team_member in self._developers  # implement __eq__ to compare objects
        ):  # We dont want to access self_developers, we need descriptors or properties
            self._developers.add(team_member)

    def remove(self, team_member: "Employee" | "Developer") -> None:
        """Remove a developer - Side Effect"""
        self._developers.discard(team_member)
