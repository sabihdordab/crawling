from django import forms

class ScraperSelectionForm(forms.Form):
    scraper_choices = [
        ('divar', 'Divar'), 
    ]
    scraper = forms.ChoiceField(choices=scraper_choices, label='Select Scraper')
