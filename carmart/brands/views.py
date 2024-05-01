from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required

@login_required
def add_brand(request):
    if request.method == 'POST':
        brand_form = forms.BrandsForm(request.POST)
        if brand_form.is_valid():
            brand_form.instance.author = request.user
            brand_form.save()
            return redirect('add_car')
    else:
      brand_form = forms.BrandsForm()

    return render(request, 'brands/add_brand.html', {'form2': brand_form})