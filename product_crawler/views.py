from django.shortcuts import render, redirect
from .forms import ScraperSelectionForm
from .scrapers import DivarScraper  
from . models import Product

def scraper_view(request):
    if request.method == 'POST':
        form = ScraperSelectionForm(request.POST)
        if form.is_valid():
            scraper_choice = form.cleaned_data['scraper']
            if scraper_choice == 'divar':
                divar_scraper = DivarScraper()
                divar_scraper.run()
                return redirect('scraper_view')
    else:
        form = ScraperSelectionForm()
        products = Product.objects.all()  
    return render(request, 'product_list.html', {'form': form, 'products': products})
