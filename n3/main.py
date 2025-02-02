from student import Student

def main():
    author = Student("Леонид",
                     2,
                     {
                      "Человек и мир": [2,3,4,9,9],
                      "Математика": [6],
                      "Что-то еще":[4,10,10]
                      }
                     )
    print(author.get_avg_grade())
    print(author.get_avg_score_by_subject("Математика"))
    print(author.is_honor_student())

    second_student = Student("Гоша",
                             1,
                             {
                              "Все предметы":[10,10,10]
                              }
                             )
    print(second_student.is_honor_student())
    print(Student.get_student_quantity())

if __name__=="__main__":
    main()