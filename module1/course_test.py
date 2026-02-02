"""
course_test.py - Completed Course class implementation for testing
Used to verify the module deliverables run correctly.
"""


class Course:
    """Represents a college course with its associated data."""

    def __init__(self, name: str, code: str, credits: int,
                 instructor: str, is_online: bool):
        """Initialize a Course with all its data."""
        self._name = name
        self._code = code
        self.set_credits(credits)  # Use setter for validation
        self._instructor = instructor
        self._is_online = is_online

    # Getters
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

    # Setters
    def set_name(self, name: str) -> None:
        """Set the course name."""
        self._name = name

    def set_code(self, code: str) -> None:
        """Set the course code."""
        self._code = code

    def set_credits(self, credits: int) -> None:
        """Set the credit hours with validation (clamped to 1-5)."""
        if credits < 1:
            self._credits = 1
        elif credits > 5:
            self._credits = 5
        else:
            self._credits = credits

    def set_instructor(self, instructor: str) -> None:
        """Set the instructor name."""
        self._instructor = instructor

    def set_is_online(self, is_online: bool) -> None:
        """Set the online status."""
        self._is_online = is_online

    def __str__(self) -> str:
        """Return a formatted string representation of the course."""
        mode = "Online" if self._is_online else "In-Person"
        return f"{self._code}: {self._name} ({self._credits} credits) - {self._instructor} [{mode}]"
