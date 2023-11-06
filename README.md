# Object Oriented Programming - Python

### Python - Code Execution

The "Python Interpreter and runtime environment" work together to reads and processes code in the following stages

1. Source Code - Python code resides in a .py file or in the python interpreter.
2. Lexical Analysis - 
3. Parsing -
4. Creating the Abstract Syntax Tree - 
5. Compilation to Bytecode - The bytecode is stored in .pyc files.
6. Execution by the Python Virtual Machine (PVM) - The bytecode is executed by the PVM. The PVM is responsible for interpreting and executing the code.
    1. Dymanic Typing and Memory Management
    2. Running the code - Code execution starts from top to bottom.
    3. Input and output interaction
    4. Exception Handling
    5. Termination 
### Python - Typing
<dl>
    <dt>Duck Typing</dt>
    <dd>
        "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." 
        In Python, the type or class of an object is determined by its behavior rather that its explicit type. At runtime, the type of the object is determined based on how it is used in the code.
    </dd>
    <dt>Dynamic Typing</dt>
    <dd>
        The type of a variable is determined at runtime, not at the time the code is written or compiled.
        This flexibility allows you to reassign variables to different types without requiring explicit type declarations. 
    </dd>
    <dt>Strong Typing</dt>
    <dd>
        Python will not allow operations involving incompatible types. Such of operations will result in a TypeError. Python enforces type safety, and it does not perform implicit type conversion in most cases. 
    </dd>
</dl>

### Understanding Python's Scopes and Namespaces

### Features:
<dl>
    <dt>Class/Objects</dt>
    <dd>
        <em><strong>Instance</strong></em> variables and methods,
        <em><strong>Class</strong></em> variable and methods, and 
        <em><strong>Static</strong></em> variables and methods.
    </dd>
    <dt>Encapsulation</dt>
    <dd>
        Data hiding is not as strict in Python. (Conventions or Dataclasses approach).
    </dd>
    <dt>Inheritance</dt>
    <dd>
        Single and Multiple Inheritance.
    </dd>
    <dt>Polymorphism</dt>
    <dd>
        Overriding and Overloading.
    </dd>
    <dt>Abstraction</dt>
    <dd>
        ABC Abstraction
    </dd>
</dl>