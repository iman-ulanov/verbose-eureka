from datetime import timedelta

from django.db import models



class Language(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название курса')
    month_to_learn = models.IntegerField(verbose_name='Продолжительность курсов')

    def save(self, *args, **kwargs):
        if self.name.islower():
            self.name.title()
        super().save(*args, **kwargs)



    def __str__(self):
        return f'{self.name}-{self.month_to_learn}'




class AbstractPerson(models.Model):
    name = models.CharField(max_length=40, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')


    def save(self, *args, **kwargs):
        if self.phone_number[0] == '0':
            self.phone_number = '+996' + self.phone_number[1:10]
        super().save(*args, **kwargs)





    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}-{self.email}'


class Student(AbstractPerson):
    oss = (
        ('mac', 'MacOS'),
        ('windows', 'Windows'),
        ('linux', 'Linux')
    )
    work_study_place = models.CharField(max_length=50, null=True, blank=True, verbose_name='Место работы/учебы')
    has_own_notebook = models.BooleanField(verbose_name='Имеет ли свой ноутбук', default=False)
    preferred_os = models.CharField(max_length=30, verbose_name='Предпочитаемая ОС', choices=oss)

    def __str__(self):
        return f'{self.name}-{self.work_study_place}'


class Mentor(AbstractPerson):
    students = models.ManyToManyField(Student, related_name='studs', through='Course')
    main_work = models.CharField(max_length=40, verbose_name='Основное место работы', null=True, blank=True)
    experience = models.DateField(verbose_name='Опыт работы')

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='Наименование курса')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField(verbose_name='Дата начала курса')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentors')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)


    def __str__(self):
        f'{self.student.name} учится у {self.mentor.name}'


    def get_end_date(self):
        days = self.language.month_to_learn * 30
        date_end = self.date_started + timedelta(days=days)
        return f'У студента {self.student.name} курс заканчивается {date_end}'





