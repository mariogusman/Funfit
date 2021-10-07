from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        #defines the model and fields to be included
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        #override/change fields below using friendly names
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        #will show friendly names instead of ids
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'