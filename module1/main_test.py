"""
main_test.py - Test driver for Course class
Used to verify the module deliverables run correctly.

To run: python main_test.py
"""

from course_test import Course


def main():
    print("=== CSC 249 Module 1: Python Test ===")
    print()

    # Test creating Course objects
    print("--- Testing Course Object Creation ---")
    data_structures = Course("Data Structures", "CSC 249-0901", 3, "Dr. Smith", True)
    intro_cpp = Course("Introduction to C++", "CSC 134-0001", 3, "Prof. Johnson", False)
    calculus = Course("Calculus II", "MAT 172-0001", 4, "Dr. Lee", False)

    print("Created 3 Course objects successfully.")
    print()

    # Test getters
    print("--- Testing Getters ---")
    print(f"Course name: {data_structures.get_name()}")
    print(f"Course code: {data_structures.get_code()}")
    print(f"Credits: {data_structures.get_credits()}")
    print(f"Instructor: {data_structures.get_instructor()}")
    print(f"Is Online: {'Yes' if data_structures.get_is_online() else 'No'}")
    print()

    # Test setters
    print("--- Testing Setters ---")
    data_structures.set_instructor("Dr. Williams")
    print(f"New instructor: {data_structures.get_instructor()}")

    # Test validation
    print("Testing credits validation...")
    data_structures.set_credits(10)
    print(f"After setting to 10, credits are: {data_structures.get_credits()} (should be 5)")
    data_structures.set_credits(0)
    print(f"After setting to 0, credits are: {data_structures.get_credits()} (should be 1)")
    data_structures.set_credits(3)
    print(f"After setting to 3, credits are: {data_structures.get_credits()} (should be 3)")
    print()

    # Test __str__
    print("--- Testing __str__() ---")
    print(data_structures)
    print(intro_cpp)
    print(calculus)
    print()

    # Test list of objects
    print("--- Testing Objects in List ---")
    courses = [data_structures, intro_cpp, calculus]

    print("All courses:")
    for course in courses:
        print(f"  {course}")

    # Test sorting
    print("\nSorted by name:")
    courses_sorted = sorted(courses, key=lambda c: c.get_name())

    for course in courses_sorted:
        print(f"  {course}")

    print()
    print("=== All Tests Passed ===")


if __name__ == "__main__":
    main()
