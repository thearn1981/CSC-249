# Module 1: Supplemental Notes

## Deep Dive on Object-Oriented Programming Concepts

These notes expand on the main lecture material for students who want a more thorough understanding or who are transitioning between C++ and Python.

---

## Table of Contents

1. [OOP Terminology Glossary](#oop-terminology-glossary)
2. [C++ vs Python: Detailed Syntax Comparison](#c-vs-python-detailed-syntax-comparison)
3. [Constructors: Default vs. Parameterized](#constructors-default-vs-parameterized)
4. [The `this` Pointer / `self` Reference](#the-this-pointer--self-reference)
5. [Common Pitfalls and How to Avoid Them](#common-pitfalls-and-how-to-avoid-them)
6. [When to Use Getters and Setters](#when-to-use-getters-and-setters)
7. [Memory and Object Lifetime](#memory-and-object-lifetime)
8. [Preview: How Data Structures Use These Concepts](#preview-how-data-structures-use-these-concepts)

---

## OOP Terminology Glossary

| Term | Definition | Example |
|------|------------|---------|
| **Class** | A blueprint/template for creating objects | `class Course { ... }` |
| **Object** | A specific instance of a class | `Course myCourse("DS", "CSC249", 3, "Smith", true);` |
| **Instance** | Synonym for object | Same as above |
| **Attribute** | A variable that belongs to an object (state) | `name`, `credits` |
| **Member variable** | C++ term for attribute | `std::string name;` |
| **Instance variable** | Python term for attribute | `self._name` |
| **Method** | A function that belongs to a class (behavior) | `getName()`, `setCredits()` |
| **Member function** | C++ term for method | Same as above |
| **Constructor** | Special method that initializes a new object | `Course(...)` / `__init__(...)` |
| **Getter** | Method that returns an attribute's value | `getName()` |
| **Setter** | Method that modifies an attribute's value | `setName(...)` |
| **Encapsulation** | Hiding internal details, exposing controlled interface | Private attributes + public methods |
| **Access modifier** | Keyword controlling visibility | `private`, `public`, `protected` |

---

## C++ vs Python: Detailed Syntax Comparison

### Class Declaration

**C++ (header file)**
```cpp
// Course.h
#ifndef COURSE_H
#define COURSE_H

#include <string>

class Course {
private:
    std::string name;
    std::string code;
    int credits;
    std::string instructor;
    bool isOnline;

public:
    // Constructor
    Course(std::string name, std::string code, int credits,
           std::string instructor, bool isOnline);

    // Getters
    std::string getName() const;
    std::string getCode() const;
    int getCredits() const;
    std::string getInstructor() const;
    bool getIsOnline() const;

    // Setters
    void setName(std::string name);
    void setCode(std::string code);
    void setCredits(int credits);
    void setInstructor(std::string instructor);
    void setIsOnline(bool isOnline);

    // Display
    std::string toString() const;
};

#endif
```

**Python**
```python
# course.py

class Course:
    """Represents a college course."""

    def __init__(self, name: str, code: str, credits: int,
                 instructor: str, is_online: bool):
        self._name = name
        self._code = code
        self._credits = credits
        self._instructor = instructor
        self._is_online = is_online

    # Getters
    def get_name(self) -> str:
        return self._name

    def get_code(self) -> str:
        return self._code

    def get_credits(self) -> int:
        return self._credits

    def get_instructor(self) -> str:
        return self._instructor

    def get_is_online(self) -> bool:
        return self._is_online

    # Setters
    def set_name(self, name: str) -> None:
        self._name = name

    def set_code(self, code: str) -> None:
        self._code = code

    def set_credits(self, credits: int) -> None:
        self._credits = credits

    def set_instructor(self, instructor: str) -> None:
        self._instructor = instructor

    def set_is_online(self, is_online: bool) -> None:
        self._is_online = is_online

    # Display
    def __str__(self) -> str:
        mode = "Online" if self._is_online else "In-Person"
        return f"{self._code}: {self._name} ({self._credits} credits) - {self._instructor} [{mode}]"
```

### Key Differences Explained

| Aspect | C++ | Python |
|--------|-----|--------|
| **Privacy enforcement** | Compiler-enforced (`private:`) | Convention only (`_` prefix) |
| **File organization** | Often split: `.h` (declaration) + `.cpp` (implementation) | Single `.py` file |
| **Type declarations** | Required: `std::string name;` | Optional hints: `name: str` |
| **Constructor name** | Same as class name: `Course(...)` | Always `__init__(self, ...)` |
| **Self reference** | Implicit `this->` (often omitted) | Explicit `self.` required |
| **String formatting** | `std::to_string()` + concatenation | f-strings: `f"{value}"` |
| **Boolean type** | `bool` with `true`/`false` | `bool` with `True`/`False` |
| **Method const-ness** | `const` keyword for read-only methods | No equivalent |

---

## Constructors: Default vs. Parameterized

### What is a Constructor?

A constructor is a special method that runs automatically when you create a new object. Its job is to initialize the object's state.

### Parameterized Constructor

Takes arguments to set initial values:

**C++**
```cpp
Course::Course(std::string name, std::string code, int credits,
               std::string instructor, bool isOnline) {
    this->name = name;
    this->code = code;
    setCredits(credits);  // Use setter for validation
    this->instructor = instructor;
    this->isOnline = isOnline;
}

// Usage:
Course ds("Data Structures", "CSC 249", 3, "Dr. Smith", true);
```

**Python**
```python
def __init__(self, name: str, code: str, credits: int,
             instructor: str, is_online: bool):
    self._name = name
    self._code = code
    self.set_credits(credits)  # Use setter for validation
    self._instructor = instructor
    self._is_online = is_online

# Usage:
ds = Course("Data Structures", "CSC 249", 3, "Dr. Smith", True)
```

### Default Constructor

Takes no arguments, uses default values:

**C++**
```cpp
Course::Course() {
    name = "Unknown";
    code = "XXX 000";
    credits = 3;
    instructor = "TBD";
    isOnline = false;
}

// Usage:
Course empty;  // Creates course with default values
```

**Python**
```python
def __init__(self, name: str = "Unknown", code: str = "XXX 000",
             credits: int = 3, instructor: str = "TBD",
             is_online: bool = False):
    # ... same as before

# Usage:
empty = Course()  # Creates course with default values
partial = Course("Calc", "MAT 171")  # Uses defaults for rest
```

### Which Should You Use?

**It depends on your needs:**

- **Parameterized only**: When objects must have valid data from the start
- **Default only**: When you'll set values later via setters
- **Both**: Maximum flexibility (common in C++)
- **Default parameters** (Python): Combines both approaches elegantly

For our `Course` class, we use a parameterized constructor because a course without a name or code isn't meaningful.

---

## The `this` Pointer / `self` Reference

When you're inside a method, how do you refer to the object the method belongs to?

### C++: `this` Pointer

```cpp
void Course::setName(std::string name) {
    this->name = name;  // this->name is the member variable
                        // name is the parameter
}
```

The `this->` is often optional when there's no ambiguity:

```cpp
std::string Course::getName() const {
    return name;  // Unambiguous, so this-> not needed
}
```

### Python: `self` Reference

```python
def set_name(self, name: str) -> None:
    self._name = name  # self._name is the instance variable
                       # name is the parameter
```

In Python, `self` is **always required** — it's the first parameter of every method:

```python
def get_name(self) -> str:  # self is required even with no other params
    return self._name
```

### Why the Difference?

C++ was designed to minimize typing; the compiler figures out when you mean the object's variable. Python was designed to be explicit; you always spell out what you're referring to.

Neither approach is "better" — they reflect different design philosophies.

---

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Forgetting to Initialize Variables

**C++ Problem:**
```cpp
Course::Course(std::string n, std::string c, int cr,
               std::string i, bool o) {
    name = n;
    code = c;
    // Forgot credits, instructor, isOnline!
}
// credits will have garbage value
```

**Solution:** Initialize ALL member variables, or use member initializer lists:
```cpp
Course::Course(std::string n, std::string c, int cr,
               std::string i, bool o)
    : name(n), code(c), credits(cr), instructor(i), isOnline(o) {
    // Body can be empty if using initializer list
}
```

**Python Problem:**
```python
def __init__(self, name, code, credits, instructor, is_online):
    self._name = name
    self._code = code
    # Forgot the rest!
# Accessing self._credits later will raise AttributeError
```

**Solution:** Always initialize all instance variables in `__init__`.

### Pitfall 2: Shadowing (Name Collision)

**C++ Problem:**
```cpp
void Course::setName(std::string name) {
    name = name;  // This does nothing! Assigns parameter to itself.
}
```

**Solution:** Use `this->`:
```cpp
void Course::setName(std::string name) {
    this->name = name;
}
```

**Python**: Less of an issue because `self.` is required, but still be careful with local variables.

### Pitfall 3: Returning References to Private Data (C++)

**Problem:**
```cpp
std::string& Course::getName() {
    return name;  // Returns reference to private data!
}

// External code can now modify it:
course.getName() = "Hacked!";  // Bypasses setter!
```

**Solution:** Return by value or const reference:
```cpp
std::string Course::getName() const {
    return name;  // Returns a copy
}

// Or:
const std::string& Course::getName() const {
    return name;  // Returns read-only reference
}
```

### Pitfall 4: Mutable Default Arguments (Python)

**Problem:**
```python
def __init__(self, name, tags=[]):  # DON'T DO THIS
    self._tags = tags
```

The empty list `[]` is created once and shared by all instances!

**Solution:** Use `None` as default:
```python
def __init__(self, name, tags=None):
    self._tags = tags if tags is not None else []
```

---

## When to Use Getters and Setters

### Always Use Them When:

1. **Validation is needed**: setCredits must check range
2. **Side effects are needed**: Setting a value might trigger logging or updates
3. **You might change internal representation**: Future flexibility
4. **Building a library/API**: External users shouldn't depend on internals

### Consider Skipping Them When:

1. **Simple data containers**: A `Point` with just `x` and `y` might not need them
2. **Internal/private classes**: Not exposed outside your code
3. **Performance-critical code**: Getter/setter overhead matters (rare)

### Python Alternative: Properties

Python offers `@property` decorators as a middle ground:

```python
class Course:
    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        if value < 1:
            self._credits = 1
        elif value > 5:
            self._credits = 5
        else:
            self._credits = value

# Usage looks like direct access:
course.credits = 10  # Actually calls the setter
print(course.credits)  # Actually calls the getter
```

We use explicit `get_`/`set_` methods in this course to parallel C++ and make the method calls visible.

---

## Memory and Object Lifetime

### C++: Stack vs. Heap

**Stack allocation** (automatic):
```cpp
void example() {
    Course ds("Data Structures", "CSC 249", 3, "Smith", true);
    // ds exists until end of this function
}  // ds is automatically destroyed here
```

**Heap allocation** (manual):
```cpp
void example() {
    Course* ds = new Course("Data Structures", "CSC 249", 3, "Smith", true);
    // ds exists until you delete it
    delete ds;  // Must manually free memory
}
```

For this course, we'll primarily use stack allocation. Heap allocation becomes important with data structures (nodes in linked lists, etc.).

### Python: Automatic Memory Management

Python handles memory automatically via reference counting and garbage collection:

```python
def example():
    ds = Course("Data Structures", "CSC 249", 3, "Smith", True)
    # ds exists as long as something references it

# When function ends, if nothing else references ds,
# Python automatically frees the memory
```

You generally don't need to think about memory in Python, which is one of its advantages for learning algorithms.

---

## Preview: How Data Structures Use These Concepts

Everything we've covered forms the foundation for data structures:

### Linked List Node

```cpp
class Node {
private:
    int data;       // State: the value stored
    Node* next;     // State: pointer to next node

public:
    Node(int data);
    int getData() const;
    Node* getNext() const;
    void setNext(Node* next);
};
```

### Binary Tree Node

```cpp
class TreeNode {
private:
    int data;
    TreeNode* left;
    TreeNode* right;

public:
    TreeNode(int data);
    // ... getters and setters
};
```

### Hash Table Entry

```cpp
class Entry {
private:
    std::string key;
    int value;

public:
    Entry(std::string key, int value);
    std::string getKey() const;
    int getValue() const;
    void setValue(int value);
};
```

Notice the pattern: each data structure is built from classes with:
- **Private state** (the data and links to other nodes)
- **Public behavior** (controlled access to that state)

Mastering classes and objects now will make learning these structures much smoother.

---

## Summary

| Concept | Key Takeaway |
|---------|--------------|
| **Classes** | Blueprints that define state + behavior |
| **Objects** | Instances of classes with actual data |
| **Encapsulation** | Hide internals, expose controlled interface |
| **Constructors** | Initialize objects to valid state |
| **Getters/Setters** | Controlled access with validation |
| **this/self** | Reference to the current object |

These fundamentals appear in every data structure we'll study. Take time to get comfortable with them now — it's an investment that pays off all semester.
