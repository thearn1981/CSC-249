"""
course.py - Course class definition
CSC 249 - Module 1: Classes and Objects

This file contains a skeleton for the Course class.
Your task: Implement the getters, setters, and __str__() method.

A Course object bundles together all the data for a single course,
keeping related information together so it can be sorted, searched,
and manipulated as a unit.
"""


class Course:
    """
    Represents a college course with its associated data.

    Attributes (private by convention - use underscore prefix):
        _name (str): Course title, e.g., "Data Structures"
        _code (str): Course code, e.g., "CSC 249-0901"
        _credits (int): Credit hours (valid range: 1-5)
        _instructor (str): Instructor name
        _is_online (bool): True if online, False if in-person
    """

    def __init__(self, name: str, code: str, credits: int,
                 instructor: str, is_online: bool):
        """
        Initialize a Course with all its data.

        Args:
            name: The course title
            code: The course code
            credits: Credit hours (will be clamped to 1-5)
            instructor: The instructor's name
            is_online: Whether the course is delivered online
        """
        
        self._name = name
        self._code = code
        self.set_credits(credits)
        self._instructor = instructor
        self._is_online = is_online



        

    # === GETTERS ===
    # These provide read-only access to private instance variables.
    # In Python, we often use @property decorators, but we'll use
    # explicit getter methods here to parallel the C++ version.

    def get_name(self) -> str:
        """Return the course name."""
       
        return self._name  

    def get_code(self) -> str:
        """Return the course code."""
        
        return self._code
    
    def get_credits(self) -> int:
        """Return the credit hours."""
        
        return self._credits

    def get_instructor(self) -> str:
        """Return the instructor name."""
        
        return self._instructor

    def get_is_online(self) -> bool:
        """Return whether the course is online."""
        return self._is_online

    # === SETTERS ===
    # These allow controlled modification of private instance variables.

    def set_name(self, name: str) -> None:
        """Set the course name."""
        # TODO: Set the course name
        pass

    def set_code(self, code: str) -> None:
        """Set the course code."""
        # TODO: Set the course code
        pass

    def set_credits(self, credits: int) -> None:
        """
        Set the credit hours with validation.

        Credits are clamped to the range 1-5:
        - If credits < 1, set to 1
        - If credits > 5, set to 5
        - Otherwise, use the provided value

        NOTE: This simple clamping approach is a stopgap. In production code,
        you might raise an exception to alert the caller of invalid input.
        We'll cover exception handling in a later module.
        """
        # TODO: Set the credit hours WITH VALIDATION
        pass

    def set_instructor(self, instructor: str) -> None:
        """Set the instructor name."""
        # TODO: Set the instructor name
        pass

    def set_is_online(self, is_online: bool) -> None:
        """Set the online status."""
        # TODO: Set the online status
        pass

    # === DISPLAY ===

    def __str__(self) -> str:
        """
        Return a formatted string representation of the course.

        Format: "CODE: Name (X credits) - Instructor [Online/In-Person]"
        Example: "CSC 249-0901: Data Structures (3 credits) - Dr. Smith [Online]"

        NOTE: Some designs choose to separate display/UI logic into a different
        class or layer. For simplicity, we include it here via __str__().
        This is a common pattern for simple classes, but be aware that larger
        systems may benefit from separating "what the data is" from "how it's
        displayed."

        Returns:
            A human-readable string representation of the course.
        """
        # TODO: Return a formatted string representation
        # HINT: Use an f-string for easy formatting
        # HINT: Use a conditional expression for Online/In-Person:
        #       "Online" if self._is_online else "In-Person"

        return ""  # Replace this
