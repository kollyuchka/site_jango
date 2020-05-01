from django import forms

class Form_one(forms.Form):
    file_1 = forms.FileField(label="Без рафта в режиме вазы, сохраняем в файл и загружаем. 1 файл:")
    file_2 = forms.FileField(label="Без рафта в обычном режиме, задаем три слоя top solid layers и загружаем. 2 файл")
    file_3 = forms.FileField(label="С 5-ю слоями рафта в режиме вазы, сохраняем и загружаем. 3 файл")
    file_4 = forms.FileField(label="С 5-ю слоями рафта в обычном режиме, сохраняем и загружаем. 4 файл ")

    stack_height = forms.IntegerField(label = 'STACK_HEIGHT',min_value = 0, max_value = 5, initial= 1)
    botton_solid_layer = forms.FloatField(label = 'BOTTOM_SOLID_LAYER',min_value = 10, max_value = 30, initial= 19.75)
    top_solid_layer = forms.FloatField(label = 'TOP_SOLID_LAYER',min_value = 10, max_value = 30, initial= 21.25)
    top_raft_layer = forms.FloatField(label = 'TOP_RAFT_LAYER',min_value = 0, max_value = 5, initial= 1.75)
    top_bridge_layer = forms.FloatField(label = 'TOP_BRIDGE_LAYER',min_value = 0, max_value = 5, initial=2.35)
