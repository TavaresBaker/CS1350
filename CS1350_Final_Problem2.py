class Student:
    """
    A class to represent a student and their grades.
    """

    def __init__(self, name, student_id):
        """
        Initialize a student with name and ID.
        Start with an empty list of grades.
        """
        self.name = name
        self.student_id = student_id
        self.grades = []  # empty list

    def add_grade(self, grade):
        """
        Add a grade to the student's record.
        Only add if grade is between 0 and 100.
        Returns True if added, False otherwise.
        """
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False

    def calculate_average(self):
        """
        Calculate the student's average grade.
        Returns 0 if no grades exist.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        """
        Get student's pass/fail status.
        """
        if not self.grades:
            return "No grades"

        avg = self.calculate_average()
        return "Passing" if avg >= 70 else "Failing"


