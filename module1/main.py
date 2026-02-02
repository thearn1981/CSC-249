"""
main.py - Driver program for Course class
CSC 249 - Module 1: Classes and Objects

This program tests your Course class implementation.
Complete the TODOs below after implementing course.py.

To run: python main.py
"""

from course import Course


def main():
    print("=== CSC 249 Module 1: Classes and Objects ===")
    print()

    # =========================================================================
    # PART 1: Creating Course Objects
    # =========================================================================
    print("--- Part 1: Creating Course Objects ---")

    # Example: Creating a Course object (this one is done for you)
    data_structures = Course("Data Structures", "CSC 249-0901", 3,
                             "Dr. Smith", True)

    # TODO 1: Create a Course object for "Introduction to C++"
    #         Code: "CSC 134-0001", Credits: 3, Instructor: "Prof. Johnson"
    #         This course is NOT online (in-person).
    # intro_cpp = Course(...)


    # TODO 2: Create a Course object for a course YOU are currently taking
    #         Use real or made-up data - your choice!
    # my_course = Course(...)


    print("Created 3 Course objects.")
    print()

    # =========================================================================
    # PART 2: Using Getters
    # =========================================================================
    print("--- Part 2: Using Getters ---")

    # Example: Using getters to access data
    print(f"Course name: {data_structures.get_name()}")
    print(f"Course code: {data_structures.get_code()}")

    # TODO 3: Print the credits and instructor for the intro_cpp course
    #         Use the appropriate getter methods.
    # print(f"Intro C++ credits: {intro_cpp.get_credits()}")
    # print(f"Intro C++ instructor: {intro_cpp.get_instructor()}")


    # TODO 4: Print whether your course (my_course) is online or in-person
    #         HINT: get_is_online() returns a bool, so you might want to use
    #         a conditional expression to print "Online" or "In-Person"
    # status = "Online" if my_course.get_is_online() else "In-Person"
    # print(f"My course is: {status}")

    print()

    # =========================================================================
    # PART 3: Using Setters
    # =========================================================================
    print("--- Part 3: Using Setters ---")

    # Example: Using a setter to modify data
    print("Changing Data Structures instructor...")
    data_structures.set_instructor("Dr. Williams")
    print(f"New instructor: {data_structures.get_instructor()}")

    # TODO 5: Change the intro_cpp course to be online (it was in-person)
    #         Then print confirmation using the getter.
    # intro_cpp.set_is_online(True)
    # status = "Online" if intro_cpp.get_is_online() else "In-Person"
    # print(f"Intro C++ is now: {status}")


    # TODO 6: Test the validation! Try setting credits to an invalid value.
    #         Set data_structures credits to 10 (invalid - should clamp to 5)
    #         Then print the actual value to verify clamping worked.
    # data_structures.set_credits(10)
    # print(f"After setting to 10, credits are: {data_structures.get_credits()}")

    print()

    # =========================================================================
    # PART 4: Using __str__()
    # =========================================================================
    print("--- Part 4: Using __str__() ---")

    # Example: Using __str__() for formatted output
    # In Python, print() automatically calls __str__() on objects
    print(data_structures)

    # TODO 7: Print the intro_cpp and my_course objects
    #         Just use print() - Python will call __str__() automatically!
    # print(intro_cpp)
    # print(my_course)

    print()

    # =========================================================================
    # PART 5: Objects in a Collection (Preview of Coming Attractions)
    # =========================================================================
    print("--- Part 5: Why Objects Matter ---")

    # This demonstrates why objects are better than parallel arrays.
    # When we put objects in a list, all the data stays together!

    courses = [data_structures]
    # TODO 8: Add your other two courses to the list
    # courses.append(intro_cpp)
    # courses.append(my_course)

    print("All courses in the list:")
    for course in courses:
        print(f"  {course}")

    # Sorting by name - notice how all the data stays together!
    # (We'll learn more about sorting algorithms in Module 3)
    print("\nSorted by name:")
    courses_sorted = sorted(courses, key=lambda c: c.get_name())

    for course in courses_sorted:
        print(f"  {course}")

    print()
    print("=== End of Module 1 Demo ===")


if __name__ == "__main__":
    main()
