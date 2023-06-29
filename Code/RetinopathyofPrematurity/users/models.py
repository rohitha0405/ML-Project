from django.db import models

# Create your models here.

class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'

class UserLinearResultModel(models.Model):
    name = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=100)
    precesion = models.CharField(max_length=100)
    recall = models.CharField(max_length=100)
    chitest = models.CharField(max_length=100)


    def __str__(self):
        return self.id

    class Meta:
        db_table = 'LinearResults'

class UserGA2MResultModel(models.Model):
    name = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    deviance = models.CharField(max_length=100)
    pearson_chi2 = models.CharField(max_length=100)
    llf = models.CharField(max_length=100)


    def __str__(self):
        return self.id

    class Meta:
        db_table = 'GA2MResults'
