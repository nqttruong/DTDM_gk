from django import forms
from .models import Coffee
class AddCoffeeForm(forms.ModelForm):
	name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
	price = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Price", "class":"form-control"}), label="")
	# quantity = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity", "class":"form-control"}), label="")
	image = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Image", "class":"form-control"}), label="")
	
	class Meta:
		model = Coffee
		exclude = ("user", "quantity" )

class OrderCoffeeForm(forms.ModelForm):
	quantity = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity", "class":"form-control"}), label="")
	class Meta:
		model = Coffee
		exclude = ("user", "name", "price", "image")