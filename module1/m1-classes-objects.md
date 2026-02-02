# Module 1: Classes and Objects

## Why This Matters

You're juggling multiple courses this semester. Each course has a name, a code, credits, an instructor, and a delivery mode. How do you keep track of all that data in a program?

This module introduces **classes and objects** — the fundamental building blocks we'll use throughout this course when we study data structures like linked lists, trees, and hash tables.

---

## The Problem: Parallel Arrays

A natural first instinct is to use separate lists for each piece of data:

```
names:       ["Data Structures", "Intro to C++", "Calculus II"]
codes:       ["CSC 249-0901",    "CSC 134-0001", "MAT 172-0001"]
credits:     [3,                 3,              4]
instructors: ["Dr. Smith",       "Prof. Johnson", "Dr. Lee"]
```

This is called **parallel arrays** (or parallel lists). The correspondence between data points is maintained by index: `names[0]` goes with `codes[0]`, `credits[0]`, and `instructors[0]`.

### What Could Go Wrong?

Imagine you want to sort your courses alphabetically by name. After sorting:

```
names:       ["Calculus II", "Data Structures", "Intro to C++"]
codes:       ["CSC 249-0901", "CSC 134-0001", "MAT 172-0001"]  // NOT SORTED!
credits:     [3, 3, 4]                                         // WRONG ORDER!
```

**The names moved, but the other arrays didn't.** Now "Calculus II" appears to be "CSC 249-0901" with 3 credits — completely wrong!

You *could* sort all arrays together, but this is error-prone and becomes a nightmare as your data grows. There's a better way.

> **Try the interactive demo**: [Parallel Arrays Demo](../demo/parallel-arrays-demo.html) — see this problem happen visually, then see the solution.

---

## The Solution: Objects

Instead of keeping data in separate arrays, we bundle related data together into a single **object**:

```
Course Object 1:
    name: "Data Structures"
    code: "CSC 249-0901"
    credits: 3
    instructor: "Dr. Smith"
    is_online: true

Course Object 2:
    name: "Intro to C++"
    code: "CSC 134-0001"
    credits: 3
    instructor: "Prof. Johnson"
    is_online: false
```

Now when we sort, **the entire object moves as a unit**. The data stays together because it *is* together.

---

## Anatomy of a Class

A **class** is the blueprint for creating objects. It defines:

1. **State** (data/attributes) — the information the object holds
2. **Behavior** (methods/functions) — what the object can do

```
┌─────────────────────────────────────┐
│            Course                   │
├─────────────────────────────────────┤
│  - name: string                     │
│  - code: string                     │  ← STATE (private)
│  - credits: int                     │
│  - instructor: string               │
│  - is_online: bool                  │
├─────────────────────────────────────┤
│  + getName(): string                │
│  + setName(name): void              │
│  + getCredits(): int                │  ← BEHAVIOR (public)
│  + setCredits(credits): void        │
│  + toString(): string               │
│  ...                                │
└─────────────────────────────────────┘
```

The `-` means **private** (hidden from outside code).
The `+` means **public** (accessible to outside code).

---

## Why Private? Why Getters and Setters?

You might wonder: why not just make everything public and access it directly?

**Encapsulation** — one of the core principles of object-oriented programming — means hiding internal details and providing controlled access. This matters for:

### 1. Validation

What if someone tries to set `credits` to -5 or 100? With a setter, you can check:

```cpp
void setCredits(int credits) {
    if (credits < 1) {
        this->credits = 1;      // Clamp to minimum
    } else if (credits > 5) {
        this->credits = 5;      // Clamp to maximum
    } else {
        this->credits = credits;
    }
}
```

Direct access (`course.credits = -5`) would bypass this protection.

### 2. Future Flexibility

If you later need to change how data is stored internally, getters and setters let you do that without breaking code that uses your class.

### 3. Debugging

When something goes wrong, you can add logging to a setter to see when and where a value changes. With direct access, you'd have no single point to monitor.

---

## State vs. Behavior: A Visual Model

Think of an object as a box with two compartments:

```
┌───────────────────────────────────────┐
│              COURSE OBJECT            │
│  ┌─────────────────────────────────┐  │
│  │           STATE                 │  │
│  │  (the data it remembers)        │  │
│  │                                 │  │
│  │  name = "Data Structures"       │  │
│  │  credits = 3                    │  │
│  │  ...                            │  │
│  └─────────────────────────────────┘  │
│  ┌─────────────────────────────────┐  │
│  │          BEHAVIOR               │  │
│  │  (what it can do)               │  │
│  │                                 │  │
│  │  getName() → returns name       │  │
│  │  setCredits(n) → validates & saves│ │
│  │  toString() → formats for display│ │
│  └─────────────────────────────────┘  │
└───────────────────────────────────────┘
```

The state is **private** — outside code can't reach in and change it directly.
The behavior is **public** — it's the "interface" the object presents to the world.

---

## The Code: C++ vs. Python

Both languages support classes, but the syntax differs. Here's a side-by-side comparison of declaring a simple class:

### C++ (Course.h)
```cpp
class Course {
private:
    std::string name;
    int credits;

public:
    Course(std::string name, int credits);
    std::string getName() const;
    void setCredits(int credits);
    std::string toString() const;
};
```

### Python (course.py)
```python
class Course:
    def __init__(self, name: str, credits: int):
        self._name = name
        self._credits = credits

    def get_name(self) -> str:
        return self._name

    def set_credits(self, credits: int) -> None:
        self._credits = credits

    def __str__(self) -> str:
        return f"{self._name} ({self._credits} credits)"
```

**Key differences:**
- C++ uses `private:` and `public:` keywords; Python uses `_` prefix as a convention
- C++ separates declaration (header) from implementation; Python puts it all together
- Python's `__str__` is equivalent to a `toString()` method

See the **Supplemental Notes** for a detailed comparison.

---

## A Note on Display Logic

The `toString()` / `__str__()` method handles how the object appears when printed. This is convenient for simple classes, but be aware:

> Some designs separate "what the data is" from "how it's displayed." For example, you might have a `Course` class for data and a `CourseFormatter` class for display. This becomes important in larger systems where the same data might need to appear differently in different contexts (on screen, in a file, over a network).

For now, keeping display logic in the class is fine. We'll revisit separation of concerns as systems get more complex.

---

## Your Assignment

You'll receive a **skeleton** `Course` class with:
- Private member variables declared
- Method signatures (stubs) provided
- Comments explaining what each method should do

Your task:
1. Implement the **getters** to return each piece of data
2. Implement the **setters** (with validation for `credits`)
3. Implement **toString() / \_\_str\_\_()** for formatted display
4. Complete the **main** program to create and manipulate Course objects

This is a scaffolded exercise — we've provided the structure, you fill in the logic. By the end, you'll have working code that demonstrates why objects are better than parallel arrays.

---

## Looking Ahead

Once you're comfortable with classes and objects, you'll be ready for **data structures** — classes that organize and manage collections of data:

- **Linked Lists**: Objects (Nodes) that point to other objects
- **Stacks and Queues**: Objects that control how data enters and exits
- **Trees**: Objects arranged in parent-child hierarchies
- **Hash Tables**: Objects that enable fast lookup

Each of these is built from the same foundation you're learning now: classes with state and behavior, encapsulation, and objects that bundle data together.

---

## Resources

- [Interactive Demo: Parallel Arrays Problem](../demo/parallel-arrays-demo.html)
- [Supplemental Notes: Deep Dive on OOP Concepts](m1-supplemental-notes.md)
- [Assignment Files: cpp/ and python/](../assignment/)
