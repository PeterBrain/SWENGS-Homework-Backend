from django.db import models


class Department(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=True, blank=True) # blank has to be true, otherwise django admin cannot create a new department

    def __str__(self):
        return self.name


class Employee(models.Model):
    """CHOICES = (
        ('f', 'Finance'),
        ('it', 'IT'),
        ('hr', 'Human Resources'),
        ('m', 'Marketing')
    )"""

    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    dob = models.DateField(null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    # expertise = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
