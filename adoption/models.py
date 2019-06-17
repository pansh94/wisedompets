from django.db import models


class Pets(models.Model):
    SEX_CHOICES = [
        ('M','Male'),
        ('F','Female')
    ]
    name =  models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True) #means can exist withour a breed
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    has_reason = models.ManyToManyField(Pets, through='Reason')

    def __str__(self):
        return f"Vaccine name is {self.name}"


class Reason(models.Model):
    pets = models.ForeignKey(Pets, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    reason_for = models.TextField()

    def __str__(self):
        return (self.pets.name+" was given "+ self.vaccine.name+" vaccine for "+self.reason_for+".")
