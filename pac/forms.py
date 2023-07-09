from django import forms
from .models import Consultation


class ConsultantForm(forms.ModelForm):
    meet_date = forms.CharField(label='Tarix*',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Tarix / Saat*', 'type': 'datetime-local'}))
    name = forms.CharField(label='Ad', widget=forms.TextInput(attrs={'placeholder': 'Ad*'}))
    surname = forms.CharField(label='Soyad', widget=forms.TextInput(attrs={'placeholder': 'Soyad*'}))
    phone_number = forms.CharField(label='Əlaqə nömrəsi',
                                   widget=forms.TextInput(attrs={'placeholder': 'Əlaqə nömrəsi*', 'type': 'tel'}))
    email = forms.EmailField(label="Email ünvanı",
                             widget=forms.TextInput(attrs={'placeholder': 'Email*', 'type': 'email'}))
    gpa = forms.CharField(label='Ortalama', widget=forms.TextInput(
        attrs={'placeholder': 'Ortalama*', 'type': 'number'}))
    language_certificate = forms.CharField(label="Dil sertifikatları", widget=forms.TextInput(
        attrs={'placeholder': 'Dil sertifikatları(İELTS,TOEFL və digər)', 'type': 'text'}))
    interest_country = forms.CharField(label="Ölkə(lər)",
                                       widget=forms.TextInput(attrs={'placeholder': 'Istədiyiniz ölkə'}))
    interested_scholarship_programs = forms.CharField(label="Təqaüd proqramları",
                                                      widget=forms.TextInput(attrs={'placeholder': 'Təqaüd...'}))
    work_experience = forms.CharField(label="İş təcrübəniz",
                                      widget=forms.TextInput(attrs={'placeholder': 'Təcrübə...'}))

    class Meta:
        model = Consultation
        exclude = ("is_met",)

    def __init__(self, *args, **kwargs):
        super(ConsultantForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
            self.fields[field].required = True
        self.fields['meet_type'].label = 'Görüş tipi'
        self.fields['education_degree'].label = 'Təhsil dərəcəniz'


class MiddleContact(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ("email", "phone_number")

    def __init__(self, *args, **kwargs):
        super(MiddleContact, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({"class": "email", "placeholder": "E-mail"})
        self.fields['phone_number'].widget.attrs.update({"class": "website", "placeholder": "Əlaqə nömrəsi"})
