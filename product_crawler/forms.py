from django import forms

class ScraperSelectionForm(forms.Form):
    SCRAPER_CHOICES = [
        ('divar', 'Divar'),
        ('basalam', 'Basalam'),
        ('bamilo', 'Bamilo'),
    ]

    DIVAR_CITY_CHOICES = [
        ('tehran', 'Tehran'),
        ('tabriz', 'Tabriz'),
        ('ahvaz', 'Ahvaz'),
        ('bandar-abbas', 'Bandar Abbas'),
    ]

    DIVAR_CATEGORY_CHOICES = [
        ('vehicles', 'Vehicles'),
        ('electronic-devices', 'Electronic Devices'),
        ('watches', 'Watches'),
        ('mobile-tablet', 'Mobile & Tablet'),
        ('computers', 'Computers'),
        ('game-consoles', 'Game Consoles'),
        ('motorcycles', 'Motorcycles'),
        ('game-and-toys', 'Games & Toys'),
    ]

    BASALAM_CATEGORY_CHOICES = [
        ('mobile-phones', 'Mobile Phones'),
        ('game-console-and-accessories', 'Game Console & Accessories'),
        ('photography-camera', 'Photography & Camera'),
        ('telescope', 'Telescope'),
        ('toys', 'Toys'),
        ('converter-and-adapter', 'Converter & Adapter'),
    ]

    scraper = forms.ChoiceField(choices=SCRAPER_CHOICES, label='Select Scraper')
    divar_city = forms.ChoiceField(
        choices=DIVAR_CITY_CHOICES,
        required=False,
        label='Select City (Divar Only)'
    )
    divar_category = forms.ChoiceField(
        choices=DIVAR_CATEGORY_CHOICES,
        required=False,
        label='Select Category (Divar Only)'
    )
    basalam_category = forms.ChoiceField(
        choices=BASALAM_CATEGORY_CHOICES,
        required=False,
        label='Select Category (Basalam Only)'
    )
    limit = forms.IntegerField(
        min_value=1, 
        required=False, 
        label="Limit", 
        initial=50
    )

