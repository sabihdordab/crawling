from django.shortcuts import render, redirect
from .forms import ScraperSelectionForm
from .scrapers import DivarScraper , BamiloScraper , BasalamScraper
from . models import Product

def scraper_view(request):
    if request.method == 'POST':
        form = ScraperSelectionForm(request.POST)
        if form.is_valid():
            scraper_choice = form.cleaned_data['scraper']
            limit = form.cleaned_data['limit']
            if scraper_choice == 'divar':
                divar_city = form.cleaned_data['divar_city']
                divar_category = form.cleaned_data['divar_category']
                url = f"https://divar.ir/s/{divar_city}/{divar_category}"
                divar_scraper = DivarScraper(url=url, limit=limit)
                divar_scraper.run()

            elif scraper_choice == 'basalam': 
                basalam_category = form.cleaned_data['basalam_category']
                url = f"https://basalam.com/search/subcategory/{basalam_category}"
                basalam_scraper = BasalamScraper(url=url, limit=limit)
                basalam_scraper.run()

            elif scraper_choice == 'bamilo':
                bamilo_scraper = BamiloScraper(limit=limit)
                bamilo_scraper.run()
            return redirect('scraper_view')
    else:
        form = ScraperSelectionForm()
        products = Product.objects.all()  
    return render(request, 'product_list.html', {'form': form, 'products': products})
