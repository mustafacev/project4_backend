from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import House, Realestate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bedrooms = self.request.GET.get('bedrooms')
        bathroom = self.request.GET.get('bathroom')
        city = self.request.GET.get('city')
        state = self.request.GET.get('state')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        houses = House.objects.all()

        if bedrooms:
            houses = houses.filter(bedrooms=bedrooms)
        if bathroom:
            houses = houses.filter(bathroom=bathroom)
        if city:
            houses = houses.filter(city__icontains=city)
        if state:
            houses.filter(state__icontains=state)
        if min_price:
            houses = houses.filter(price__gte=min_price)
        if max_price:
            houses = houses.filter(price__lte=max_price)

        context['bedrooms'] = bedrooms
        context['bathroom'] = bathroom
        context['city'] = city
        context['state'] = state
        context['min_price'] = min_price
        context['max_price'] = max_price
        context['houses'] = houses

        return context


class About(TemplateView):
    template_name = "about.html"


class HouseList(TemplateView):
    template_name = "house_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["house"] = House.objects.filter(title__icontains=title)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {title}"
        else:
            context["house"] = House.objects.all()
            # default header for not searching
            context["header"] = "Trending Houses"
        return context


class HouseCreate(CreateView):
    model = House
    fields = ['title', 'img', 'address', 'favorite_house', 'realtor', 'city',
              'state', 'zipcode', 'price', 'description', 'bedrooms', 'bathroom', 'sqft']
    template_name = "house_create.html"
    success_url = "/house/"


class HouseDetail(DetailView):
    model = House
    template_name = "house_detail.html"


class HouseUpdate(UpdateView):
    model = House
    fields = ['title', 'img', 'address', 'favorite_house', 'realtor', 'city',
              'state', 'zipcode', 'price', 'description', 'bedrooms', 'bathroom', 'sqft']
    template_name = "house_update.html"
    success_url = "/house/"


class HouseDelete(DeleteView):
    model = House
    template_name = "house_delete_confirmation.html"
    success_url = "/house/"


class RealestateCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        email = request.POST.get("email")
        house = House.objects.get(pk=pk)
        Realestate.objects.create(title=title, email=email, house=house)
        return redirect('house_detail', pk=pk)


class RealtorListView(ListView):
    model = Realestate
    template_name = 'realtor_list.html'
    context_object_name = 'realtors'


class RealtorDetailView(DetailView):
    model = Realestate
    template_name = 'realtor_detail.html'
    context_object_name = 'realtor'
