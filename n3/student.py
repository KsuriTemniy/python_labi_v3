from typing import Dict, List


class Student:
    _student_quantity = 0
    _honor_grade = 8.5
    _max_course = 6
    _min_grade = 0
    _max_grade = 100

    @classmethod
    def get_student_quantity(cls, *args, **kwargs):
        return cls._student_quantity

    def __init__(self, name: str, course: int, grades: Dict[str, List[int]]):
        Student._student_quantity += 1
        self.name = name
        self.course = course
        self.grades = grades
        self.__avg_grade = self.get_avg_grade()
        self.__is_honor = self.__avg_grade > self._honor_grade

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if len(name.strip()) == 0:
            raise ValueError("Имя не должно быть пустым")
        self.__name = name.strip()

    @property
    def course(self) -> int:
        return self.__course

    @course.setter
    def course(self, course: int):
        if not isinstance(course, int):
            raise TypeError("Курс должен быть целым числом")
        if not 1 <= course <= self._max_course:
            raise ValueError(f"Курс должен быть целым числом между 1 и {self._max_course}")
        self.__course = course

    @property
    def grades(self) -> Dict[str, List[int]]:
        return self.__grades

    @grades.setter
    def grades(self, grades: Dict[str, List[int]]):
        if not isinstance(grades, dict):
            raise TypeError("Словарь оценок должны быть словарем")
        if len(grades) == 0:
            raise ValueError("Словарь оценок не должен быть пустым")

        for subject, marks in grades.items():
            if not isinstance(subject, str) or len(subject.strip()) == 0:
                raise ValueError("Название предмета не должно быть пустой строкой")
            if not isinstance(marks, list) or len(marks) == 0:
                raise ValueError("Оценки должны быть не пустым списком")
            for mark in marks:
                if not isinstance(mark, int):
                    raise TypeError("Все оценки должны быть целыми числами")
                if not self._min_grade <= mark <= self._max_grade:
                    raise ValueError(f"Оценки должны быть между {self._min_grade} и {self._max_grade}")

        self.__grades = {k.strip(): v for k, v in grades.items()}
        self.__avg_grade = self.get_avg_grade()
        self.__is_honor = self.__avg_grade > self._honor_grade

    def get_avg_grade(self) -> float:
        avg_grade = 0
        for subject in self.__grades:
            avg_grade += sum(self.__grades[subject]) / len(self.__grades[subject])
        avg_grade /= len(self.__grades)
        return round(avg_grade, 2)

    def get_avg_score_by_subject(self, subject: str) -> float:
        if subject not in self.__grades:
            raise ValueError("Неверно введено название предмета")
        return round(sum(self.__grades[subject]) / len(self.__grades[subject]), 2)

    def is_honor_student(self):
        return self.__is_honor
