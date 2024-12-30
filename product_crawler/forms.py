from django import forms

class ScraperSelectionForm(forms.Form):
    scraper_choices = [
        ('divar', 'Divar'), 
    ]
    scraper = forms.ChoiceField(choices=scraper_choices, label='Select Scraper')
    from django import forms

class ScraperSelectionForm(forms.Form):
    scraper_choices = [
        ('divar', 'Divar'), 
    ]
    scraper = forms.ChoiceField(choices=scraper_choices, label='Select Scraper')
from django import forms

class ScraperSelectionForm(forms.Form):
    scraper_choices = [
        ('divar', 'Divar'), 
    ]
    scraper = forms.ChoiceField(choices=scraper_choices, label='Select Scraper')
    from django import forms

class ScraperSelectionForm(forms.Form):
    scraper_choices = [
        ('divar', 'Divar'), 
        ('bamilo', 'Bamilo'),
    ]
    scraper = forms.ChoiceField(choices=scraper_choices, label='Select Scraper')
    limit = forms.IntegerField(min_value=1, required=False, label="Limit", initial=50)
