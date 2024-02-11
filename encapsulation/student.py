"""Student Class Definition"""
#!usr/bin/env python3
# -*- coding: UTF-8 -*-


class Student:
    """
    Class Members Definition
    Non-Public Attributes:
    - first_name
    - last_name
    - id_number
    - declare_major

    Methods:
    - retrieve_info() -> str
    """

    def __new__(cls, *args, **kwargs) -> "Student":
        """Object Creation"""
        return super().__new__(cls)

    def __init__(
        self, first_name: str, last_name: str, id_number: int, declare_major: str
    ) -> None:
        """Object State Initialization - Setting Non-Public attributes via name mangling"""
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__id_number: int = id_number
        self.__declare_major: str = declare_major

    def __repr__(self) -> str:
        """Object representation"""
        return(
            f"{type(self).__name__}:"
            f"{self.__id_number, self.__first_name, self.__last_name,self.__declare_major}"
         )

    def retrieve_info(self) -> str:
        """Retrieves the student instance information"""
        return(
            f"Fullname: {self.__first_name +" "+self.__last_name}"
            f" | id: {self.__id_number} | Major: {self.__declare_major}"
         )


def main() -> None:
    """Driver - Testing"""
    data = ["Kervi", "Ramos", 1234, "Civil Engineering"]
    obj = Student(*data)
   #  Comment: The operation below will not throw
   #  an error instead __first_name gets added to .__dict__
   # Instance attribute __first_name does not get overwritten
   #  obj.__first_name = "Mamud"
    print(obj,obj.__dict__, obj.retrieve_info(), sep="\n")


if __name__ == "__main__":
    main()
