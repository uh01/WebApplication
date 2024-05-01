from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,DetailView
from django.contrib import messages
from .models import CarsModel
from author.models import BoughtCar


@login_required
def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarsForm(request.POST)
        if car_form.is_valid():
            car_instance = car_form.save(commit=False)
            car_instance.author = request.user
            car_instance.save()
            return redirect('home')
    else:
        car_form = forms.CarsForm()

    return render(request, 'cars/add_car.html', {'form': car_form})


@method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.CarsModel
    form_class = forms.CarsForm
    template_name = 'cars/add_car.html'
    success_url = reverse_lazy('add_car')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class DetailCarView(DetailView):
    model = models.CarsModel
    pk_url_kwarg = 'id'
    template_name = 'cars/car_details.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
      comment_form = forms.CommentForm(data=self.request.POST)
      post = self.get_object()
    
      if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.car = post
        new_comment.save()

        return redirect('view_details', id=post.id)

      return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

    
@login_required
def buy_now(request, id):
    car = CarsModel.objects.get(id=id)

    if car.carQuantity > 0:
        car.carQuantity -= 1
        car.save()

        BoughtCar.objects.get_or_create(user=request.user, car=car)

        messages.success(request, f"You have successfully bought {car.carName}.")
        return redirect('view_details', id=id)