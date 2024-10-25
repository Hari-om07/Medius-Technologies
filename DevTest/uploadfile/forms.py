from django import forms

class uploadfile(forms.Form):
    file = forms.FileField(label = 'Upload Excel/CSV File')
