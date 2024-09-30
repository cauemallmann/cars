import datetime
from django import forms
from cars.models import Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ("active",)
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'O valor mínimo dos carros anunciados conosco deve ser R$10.000')
        elif value > 200000:
            self.add_error('value', 'O valor máximo dos carros anunciados conosco deve ser R$200.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1980:
            self.add_error('factory_year', 'O ano mínimo dos carros anunciados conosco deve ser 1980')
        elif factory_year > int(datetime.datetime.now().year):
            self.add_error('factory_year', f'O ano de fabrição ({factory_year}) não pode ser superior ao ano atual')
        return factory_year