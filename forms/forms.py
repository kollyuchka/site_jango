from django import forms

class Form_one(forms.Form):
    file_1 = forms.FileField(label="Без рафта в режиме вазы, сохраняем в файл и загружаем. 1 файл:")
    file_2 = forms.FileField(label="Без рафта в обычном режиме, задаем три слоя top solid layers и загружаем. 2 файл")
    file_3 = forms.FileField(label="С 5-ю слоями рафта в режиме вазы, сохраняем и загружаем. 3 файл")
    file_4 = forms.FileField(label="С 5-ю слоями рафта в обычном режиме, сохраняем и загружаем. 4 файл ")