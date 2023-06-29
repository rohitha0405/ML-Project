from django.db import models

# Create your models here.

class RetinopathyofPrematureModel(models.Model):
    gestationalweek = models.CharField(max_length=100)
    mechanicalventilation = models.CharField(max_length=100)
    bloodtransfusion = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    lateonsetsepsis = models.CharField(max_length=100)
    chorioamnionitis = models.CharField(max_length=100)
    pretermprematureruptureofmembranes = models.CharField(max_length=100)
    antenatalsteroidtherapy = models.CharField(max_length=100)
    respiratorydistresssyndrome = models.CharField(max_length=100)
    dopamindobutamin = models.CharField(max_length=100)
    necrotizingenterocolitis = models.CharField(max_length=100)
    intraventricularhemorrhage = models.CharField(max_length=100)
    constant = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)

    def __str__(self):
        return self.id
    class Meta:
        db_table = "ROPTable"















