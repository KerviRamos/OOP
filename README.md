# Object Oriented Programming - Python

### Python - Code Execution

The "Python Interpreter and runtime environment" work together to read and process code in the following steps

1. Source Code - Python code resides in a .py file or in the python interpreter.
2. Lexical Analysis 
3. Parsing
4. Creating the Abstract Syntax Tree 
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

#### Namespaces: 

1. A namespace is a mapping from names to objects.
2. The set of attributes of an object also form a namespace.
3. There is no relationship between names in different namespaces. (max(), module.max() can coexist).
4. Reference to names and functions are considered namespace attributes.
5. Attributes may be __read-only__ or __writable__. Writable attributes can be updated or deleted.
6. Namespaces are created at different moments during the execution of the program and these namespaces have different lifetimes. 
    1. The ___built-in namespace__ is created when the Python interpreter starts up and it is never deleted.
    2. The __global namespace__ for a module is created when the module definition is read and typically the module namespaces last until the interpreter quits.
    3. The __local namespace__ for a function is created when the function is called, and deleted when the function returns or raises. Recursive invocations have their own local namespace.

#### Scopes: 
1. A scope is the region where a namespace is directly accessible. 
2. At any time during execution;
    1. The innermost scope is searched first -  Contains the local names.
    2. The scope of any enclosing functions is searched next
    3. The next to last scope is the module’s namespace which contains the module’s global names.
    4. The outermost scope is searched last - Containing the built-in names.

### Features:

<dl>
    <dt>Class/Objects</dt>
    <dd>
        Class definition places another namespace in the local scope.
        Assignments are binding names to the objects.
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
