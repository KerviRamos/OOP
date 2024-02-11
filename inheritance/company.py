""" Company Object Oriented model - Inheritance"""

#!usr/bin/env python3
# -*- coding: UTF-8 -*-


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

    def __eq__(self, obj) -> bool:
        """Compare Objects"""
        if isinstance(obj, Employee):
            return (
                self._firs_name == obj._firs_name and self._last_name == obj._last_name
            )
        return False

    def fetch_details(self) -> dict[str | str, float]:
        """Summary Info - Using self.__dict__ can be problematic"""
        return {
            k: v
            for k, v in self.__dict__.items()
            if k in ["_first_name", "_last_name", "_email", "_salary"]
        }

    def update_details(self, **kwargs) -> None:
        """Update Info - Using self.__dict__ can be problematic"""
        self.__dict__.update(kwargs)


class Developer(Employee):
    """Developer definition"""

    def __new__(cls, *args, **kwargs) -> "Developer":
        """Object creation"""
        return super().__new__(cls)

    def __init__(
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
        if not team_member in self._developers:
            self._developers.add(team_member)

    def remove(self, team_member: "Employee" | "Developer") -> None:
        """Remove a developer - Side Effect"""
        self._developers.discard(team_member)
