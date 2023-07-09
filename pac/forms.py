from django import forms
from .models import Consultation


class ConsultantForm(forms.ModelForm):
    meet_date = forms.CharField(label='Tarix*',
                           widget=forms.TextInput(attrs={'placeholder': 'Tarix / Saat*', 'type': 'datetime-local'}))
    name = forms.CharField(label='Ad', widget=forms.TextInput(attrs={'placeholder': 'Ad*'}))
    surname = forms.CharField(label='Soyad', widget=forms.TextInput(attrs={'placeholder': 'Soyad*'}))
    phone_number = forms.CharField(label='Əlaqə nömrəsi',
                                   widget=forms.TextInput(attrs={'placeholder': 'Əlaqə nömrəsi*', 'type': 'tel'}))
    email = forms.EmailField(label="Email ünvanı", widget=forms.TextInput(attrs={'placeholder': 'Email*', 'type': 'email'}))
    gpa = forms.CharField(label='Ortalama', widget=forms.TextInput(
        attrs={'placeholder': 'Ortalama*', 'type': 'number'}))


    class Meta:
        model = Consultation
        exclude = ("is_met",)

    def __init__(self, *args, **kwargs):
        super(ConsultantForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})



