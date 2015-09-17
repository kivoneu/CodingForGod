from django import forms

class AddPrayerForm(forms.Form):
    prayerText = forms.CharField(label='Intencja', max_length=1024)
