from django import forms

class DjangoForm(forms.Form):
    name = forms.CharField(max_length=10, initial='Enter your name...')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':2}))
    email = forms.EmailField(label="Please Enter your Email: ", required=False)
    cleck = forms.BooleanField(initial=True)
    date = forms.DateField( widget=forms.NumberInput(attrs={'type':'date'}))
    brith_years = ['2000','2001','2003','2004']
    Cholice_your_brithday = forms.DateField(widget=forms.SelectDateWidget(years=brith_years))
    sizes = [
        ('S','Small'),
        ('L','Large'),
        ('M','midium'),
    ]
    Select_size = forms.ChoiceField(widget=forms.RadioSelect, choices=sizes)