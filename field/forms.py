from field.models import DOCUMENT, KIND, STATUS, Field
from django import forms

class FieldModelForm(forms.ModelForm):
    address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='آدرس')
    number = forms.IntegerField(label = 'قطعه شماره')
    area = forms.FloatField(label='متراژ')
    document = forms.ChoiceField(label='سند', choices=DOCUMENT)
    sale_price = forms.IntegerField(label='قیمت', required=False)
    rent_price1 = forms.IntegerField(label='رهن', required=False)
    rent_price2 = forms.IntegerField(label='اجاره', required=False)
    person = forms.CharField(widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='مسئول', required=False)
    kind = forms.ChoiceField(label='مورد جهت', choices= KIND)
    
    status = forms.ChoiceField(label='معامله شده', choices=STATUS)



    address.widget.attrs.update({'class': 'form-control'})
    number.widget.attrs.update({'class': 'form-control'})
    area.widget.attrs.update({'class': 'form-control'})
    document.widget.attrs.update({'class': 'form-control'})
    sale_price.widget.attrs.update({'class': 'form-control'})
    rent_price1.widget.attrs.update({'class': 'form-control'})
    rent_price2.widget.attrs.update({'class': 'form-control'})
    person.widget.attrs.update({'class': 'form-control'})
    kind.widget.attrs.update({'class': 'form-control'})
    status.widget.attrs.update({'class': 'form-control'})



    class Meta:
        model = Field
        fields = [
            'address',
            'number',
            'area',
            'document',
            'sale_price',
            'rent_price1',
            'rent_price2',
            'person',
            'kind',
            'status'

        ]