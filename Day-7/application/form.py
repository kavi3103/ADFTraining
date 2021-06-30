from django import forms


class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    middle_name = forms.CharField()
    last_name = forms.CharField(max_length=200)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
    gender = forms.CharField(max_length=20)
    nationality = forms.CharField(max_length=200)
    current_city = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)
    pin_code = forms.IntegerField(help_text="Enter 6 digit roll number")
    qualification = forms.CharField(max_length=200)
    salary = forms.IntegerField()
    pan = forms.CharField(max_length=10)
