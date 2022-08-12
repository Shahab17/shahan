from house.models import DOCUMENT, KIND, STATUS, House
from django import forms

class HouseModelForm(forms.ModelForm):
    address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='آدرس')
    area = forms.FloatField(label='متراژ')
    year = forms.IntegerField(label='سال')
    document = forms.ChoiceField(label='سند', choices=DOCUMENT)
    sale_price = forms.IntegerField(label='قیمت', required=False)
    rent_price1 = forms.IntegerField(label='رهن', required=False)
    rent_price2 = forms.IntegerField(label='اجاره', required=False)
    person = forms.CharField(widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='مسئول', required=False)
    kind = forms.ChoiceField(label='مورد جهت', choices= KIND)

    status = forms.ChoiceField(label='معامله شده', choices=STATUS)



    address.widget.attrs.update({'class': 'form-control'})
    area.widget.attrs.update({'class': 'form-control'})
    year.widget.attrs.update({'class': 'form-control'})
    document.widget.attrs.update({'class': 'form-control'})
    sale_price.widget.attrs.update({'class': 'form-control'})
    rent_price1.widget.attrs.update({'class': 'form-control'})
    rent_price2.widget.attrs.update({'class': 'form-control'})
    person.widget.attrs.update({'class': 'form-control'})
    kind.widget.attrs.update({'class': 'form-control'})
    status.widget.attrs.update({'class': 'form-control'})



    class Meta:
        model = House
        fields = [
            'address',
            'area',
            'year',
            'document',
            'sale_price',
            'rent_price1',
            'rent_price2',
            'person',
            'kind',
            'status'

        ]