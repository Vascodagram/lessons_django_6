from django.db import models

# Create your models here.


class Human(models.Model):

    objects = None
    CHOICE_COMPANY = (
        ('epam', 'EPAM'),
        ('google', 'Google'),
        ('apple', 'Apple')
    )

    name = models.CharField(max_length=200, verbose_name='Name')
    surname = models.CharField(max_length=200, verbose_name='Surname')
    age = models.IntegerField('Age')
    company = models.CharField(max_length=100, choices=CHOICE_COMPANY)
    salary = models.IntegerField('Salary')

    def __str__(self):
        return f'Name - {self.name} Surname - {self.surname} Company - {self.company}  '

    # def get_absolute_url(self):
    #     return f'{self.id}'
