import django.forms as forms
job_choices = [(0,'student'), (1,'employed'), (2,'unemployed'), (3,'turtle')]

class UserDataForm(forms.Form):
    name=forms.CharField(max_length=32)
    surname =forms.CharField(max_length=32)
    age =forms.IntegerField()
    mail =forms.EmailField(max_length=254)
    job =forms.ChoiceField(choices=job_choices, required=False)