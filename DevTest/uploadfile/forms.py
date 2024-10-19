from django import forms

class uploadurfile(forms.Form):
    file = forms.FileField(label = 'Upload Excel/CSV File')
