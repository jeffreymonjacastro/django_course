from django import forms
from .models import Pizza

# class PizzaForm(forms.ModelForm):
#   class Meta:
#     model = Pizza
#     fields = ['topping1', 'topping2', 'size']
#     labels = {
#       'topping1': 'Topping 1', 
#       'topping2': 'Topping 2'
#     }


class PizzaForm(forms.Form):
  toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)

  size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])