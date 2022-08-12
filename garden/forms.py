from garden.models import DOCUMENT, KIND, STATUS, Garden
from django import forms

class GardenModelForm(forms.ModelForm):
    garden = forms.CharField(max_length=100, widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='باغ')
    year = forms.IntegerField(label='سال')
    area = forms.FloatField(label='متراژ')
    address = forms.CharField(max_length=200, widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='آدرس')
    document = forms.ChoiceField(label='سند', choices=DOCUMENT)
    sale_price = forms.IntegerField(label='قیمت', required=False)
    rent_price = forms.IntegerField(label='اجاره', required=False)
    person = forms.CharField(widget=forms.Textarea(attrs={"rows": 1, "cols": 5}), label='مسئول', required=False)
    kind = forms.ChoiceField(label='مورد جهت', choices= KIND)

    status = forms.ChoiceField(label='معامله شده', choices=STATUS)


    garden.widget.attrs.update({'class': 'form-control'})
    year.widget.attrs.update({'class': 'form-control'})
    area.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    document.widget.attrs.update({'class': 'form-control'})
    sale_price.widget.attrs.update({'class': 'form-control'})
    rent_price.widget.attrs.update({'class': 'form-control'})
    person.widget.attrs.update({'class': 'form-control'})
    kind.widget.attrs.update({'class': 'form-control'})
    status.widget.attrs.update({'class': 'form-control'})



    class Meta:
        model = Garden
        fields = [
            'garden',
            'year',
            'area',
            'address',
            'document',
            'sale_price',
            'rent_price',
            'person',
            'kind',
            'status'

        ]