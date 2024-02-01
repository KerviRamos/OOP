# Object Oriented Programming - Python

### Code Execution

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

### Core OOP Features:

#### A. Classes and Objects
 In Python, classes follow a "PascalCase" naming convention. Classes are defined as the blueprint of an object. Everytime a developer defines a class, attributes and methods, the class definition creates another namespace in the local scope. Attributes refer to the properties or data associated with a specific object of a given class. Methods refer to the different behavior that an object will show. Attributes and methods are referred to as the members of a class or object.

#### B. Constructor (Instances of a Class):
The constructor is responsible for the instantiation process of an object. The instantiation process consist of two main steps; creation (overriding the "`__new__()`" dunder method) and initialization (overriding "`__init__()`" dunder method) steps.

1. Overview of the Instantiation Process:
In Python, the constructor triggers the instantiation process, which consist of two separate steps. The first step creates and returns an empty object. The second step, initalizes the objects attributes with the appropiate inital data.
In the case that, the first step, `__new__()` returns an instance of a different class; Python will not run `__init__()` dunder method for the current class.

2. Creation Step (`__new__()`):
Typically, you don't need to defined the `__new__()` dunder method eveytime you create a class. Most of the time, the base implementation of the `__new__()` dunder method, located in the 'object' base class, is enough to build an empty object of your class. If we need to subclass immutible data types, return instance of a different class, etc, we must write a custom implementation of the `__new__()` as part of our class definition. 

3. Initalization Step (`__init__()`):
The `__init__()` dunder method allows you to create an instance of the objects or a custom instance of objects. You can achieve the creation of a custom instance of the object by overriding the `__init__()` under method. It is important to validate the arguments passed through the method during the creation stage. Lastly, the init dunder method does not return any object other than None.

#### C. Public vs Non Public Members (Encapsulation):
Python does not explicitly differentiate between private, protected, and public attributes as seen in statically typed languages like Java or C++. Instead, all attributes in Python are accessible. However, Python utilizes a naming convention to achieve behavior similar to private attributes. This convention, marked by a leading underscore, either permits or restricts communication not intended for use from outside the containing class or object.

The convention involves a single leading underscore for a member's name. Another variation uses two leading underscores for the member names of the class. It's essential to note that using a single leading underscore does not prevent direct access to members within the class. Therefore, when a leading underscore is present in the members of a class, it is considered best practice to refrain from accessing the member from outside the class scope. Non-public members exist solely to support the internal implementation of a given class and may be removed at any time. Consequently, non-public members should not be used directly in any client code because they are likely to be removed or changed.

When writing a class, initially set all attributes as non-public and then make attributes public as needed for your design or use case.
Name mangling enforces non-public members by prepending the class’s name to the member’s names, like in _ClassName__attribute or _ClassName__method. This results in name hiding, preventing direct access to the member of a given class outside the class’s scope

#### D. Class and Instance Attributes:
A class can have two types of attributes;

* Class attributes:
Class attributes are defined inside the class body but outside of any method defined in the class. All of the objects created from a particular class will share the same “class” attribute with the same value. If the class attribute is changed, then that change will reflect on all created instances of the class. Class attributes can be accessed via class or via one of its instances. However, you will only be able to modify a class attribute via a class.

* Instance attributes:
Instance attributes are variables associated with a specific object of a class, meaning they are attached to the object itself. In Python, you can dynamically attach attributes to objects that have already been created.

#### E. Instance, Class, and Static Methods:

* Instance Methods:
The first parameter in the method definition is 'self.' This method is primarily used to provide the object instance behavior capabilities. The instance method can be employed to modify an object's state and even the class state through self.`__class__`.attribute

* Class Methods:
The definition of class methods requires the addition of a @classmethod decorator. The first parameter for a class method is 'cls,' unlike the 'self' parameter used in instance methods. As the class method takes the 'cls' parameter, it cannot directly modify an object's instance state. If you wish to modify the instance state, you should use methods with the 'self' parameter. These methods can be utilized to define alternative constructors for your classes.

* Static Methods:
A static method, marked with the @staticmethod decorator, doesn't require a 'self' or 'cls' parameter but can accept any number of arbitrary parameters. Unlike instance and class methods, a static method cannot modify either an object's state or a class's state. Static methods have limitations on the data they can access. They are commonly employed for utility functions that don't depend on the state of a specific instance but perform a more general task related to the class.