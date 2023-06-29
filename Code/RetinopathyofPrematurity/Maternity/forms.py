from django import forms
from .models import RetinopathyofPrematureModel


class RetinopathyofPrematureForm(forms.ModelForm):
    gestationalweek = forms.IntegerField()
    mechanicalventilation = forms.IntegerField()
    bloodtransfusion = forms.IntegerField()
    gender = forms.IntegerField()
    lateonsetsepsis = forms.IntegerField()
    chorioamnionitis = forms.IntegerField()
    pretermprematureruptureofmembranes = forms.IntegerField()
    antenatalsteroidtherapy = forms.IntegerField()
    respiratorydistresssyndrome = forms.IntegerField()
    dopamindobutamin = forms.IntegerField()
    necrotizingenterocolitis = forms.IntegerField()
    intraventricularhemorrhage = forms.IntegerField()
    constant = forms.IntegerField()
    weight = forms.IntegerField()

    class Meta:
        model = RetinopathyofPrematureModel
        fields = '__all__'
