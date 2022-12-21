import datetime
from user.models import Student, Mentor, Language, Course

lang1 = Language(name='Python', month_to_learn=6)
lang2 = Language(name='Java Script', month_to_learn=6)
lang3 = Language(name='UX-UI design', month_to_learn=2)
lang1.save()
lang2.save()
lang3.save()
stud1 = Student(name='Amanov Aman',
                               email='aman@mail.ru',
                               phone_number='+996700989898',
                               work_study_place='School №13',
                               has_own_notebook=True,
                               preferred_os='windows')
stud1.save()
stud2 = Student(name='Apina Alena',
                               email='aapina@bk.ru',
                               phone_number='0550888888',
                               work_study_place='TV',
                               has_own_notebook=True,
                               preferred_os='mac')
stud2.save()
stud3 = Student(name='Phil Spencer',
                               email='spencer@microsoft.com',
                               phone_number='0508312312',
                               work_study_place='Microsoft Gaming',
                               has_own_notebook=False,
                               preferred_os='linux')
stud3.save()

ment1 = Mentor(name='Ilona Maskova',
                              email='imask@gmail.com',
                              phone_number='0500545454',
                              main_work=None,
                              experience=datetime.date(year=2021, month=10, day=23))
ment1.save()
ment2 = Mentor(name='Halil Nurmuhametov',
                              email='halil@gmail.com',
                              phone_number='0709989876',
                              main_work='University of Fort Collins',
                              experience=datetime.date(year=2010, month=9, day=18))
ment2.save()
print('TEST')

course1 = Course(name='Python-21', language=lang1, mentor=ment2, student=stud1, date_started='2022-01-25')
course2 = Course(name='Python-21', language=lang2, mentor=ment2, student=stud2, date_started='2022-05-18')

course3 = Course(name='UXUI design-43', language=lang3, mentor=ment1, student=stud3, date_started='2022-02-05')
course1.save()
course2.save()
course3.save()