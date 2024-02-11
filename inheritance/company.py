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
    
    def __hash__(self):
        return hash((self._firs_name, self._last_name, self._salary))

    def __repr__(self) -> str:
        """Object representation"""
        return f"Full_name: {self._firs_name +" "+self._last_name} Salary: {self._salary}"

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

    def __repr__(self) -> str:
        """Object representation"""
        return f"Full_name: {self._firs_name +" "+self._last_name} Salary: {self._salary} Tech: {self._technology}"
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
        team_members: set["Employee"],
    ) -> None:
        """Object initialization"""
        super().__init__(first_name, last_name, salary)
        self._developers = team_members
        self._num_of_em = len(team_members)
    
    def __repr__(self) -> str:
        """Object representation"""
        return f"Full_name: {self._firs_name + " "+ self._last_name} Developers: {self._developers}"

    def add(self, team_member: "Employee") -> None:
        """Add a new developer - Side Effect"""
        if not team_member in self._developers:
            self._developers.add(team_member)

    def remove(self, team_member: "Employee") -> None:
        """Remove a developer - Side Effect"""
        self._developers.discard(team_member)


def main() -> None:
    """Driver - Testing"""
    employees_info = [
        ("Kervi", "Ramos", 123000),
        ("Rosa", "Ramirez", 90000),
        ("Walter", "Rumoli", 40000),
    ]
    developer_info = [
        ("Goku", "Marialee", 50000, "fullstack"),
        ("Rofilio", "Mamutee", 980000, "backend"),
        ("Kabule", "Marcona", 76000, "frontend"),
    ]
    manager_info = ("Rahulin", "Bambino", 450000)

    # Intantiating Company Ojects
    employee_objs = [Employee(*args) for args in employees_info]
    developer_objs = {Developer(*args) for args in developer_info}
    manager_obj = Manager(*manager_info, developer_objs)

    # Add and Remove an employee
    manager_obj.add(Developer("Rofilio", "Mamutee", 980000, "backend"))
    manager_obj.remove(Developer("Rofilio", "Mamutee", 980000, "backend"))

    # Temp testing
    print(employee_objs)
    print(developer_objs)
    print(manager_obj)


if __name__ == "__main__":
    main()
