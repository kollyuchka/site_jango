from django import forms

class Form_one(forms.Form):
    file_1 = forms.FileField(label="1 файл")
    file_2 = forms.FileField(label="2 файл")
    file_3 = forms.FileField(label="3 файл")
    file_4 = forms.FileField(label="4 файл")