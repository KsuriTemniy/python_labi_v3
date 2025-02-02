from typing import Dict, List

class Student:
    _student_quantity = 0
    _honor_grade = 8.5

    @classmethod
    def __call__(cls, *args, **kwargs):
        cls._student_quantity+=1

    def __init__(self, name: str, course: int, grades: Dict[str, List[int]]):
        self.__name = name
        self.__course = course
        self.__grades = grades
        self.__avg_grade = sum(grades.values())/len(grades)
        self.__is_honor = self.__avg_grade>self._honor_grade

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def course(self) -> int:
        return self.__course

    @course.setter
    def course(self, course: int):
        self.__course = course

    @property
    def grades(self) -> Dict[str, List[int]]:
        return self.__grades

    @grades.setter
    def grades(self, grades: Dict[str, List[int]]):
        self.__grades = grades
        self.__avg_grade = self.get_avg_grade()
        self.__is_honor = self.__avg_grade > self._honor_grade

    def get_avg_grade(self) -> float:
        avg_grade = 0
        for subject in self.__grades:
            avg_grade += sum(self.__grades[subject]) / len(self.__grades[subject])
        avg_grade /= len(self.__grades)
        return round(avg_grade,2)

    def get_avg_score_by_subject(self, subject: str) -> float:
        if subject not in self.__grades:
            raise ValueError("Неверно введено название предмета")
        return round(sum(self.__grades[subject]) / len(self.__grades[subject]), 2)

    def is_honor_student(self):
        return self.__is_honor
