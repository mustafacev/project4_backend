from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"
    


class About(TemplateView):
    template_name = "about.html"

class House:
    def __init__(self, title, address, realtor ,city ,state ,zipcode ,price ,description ,image ,bedrooms,bathroom ,sqft,listdate):
        self.title = title
        self.address = address
        self.realtor = realtor
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.price = price
        self.description = description
        self.image = image
        self.bedrooms = bedrooms
        self.bathroom = bathroom
        self.sqft = sqft
        self.listdate =listdate

house = [
    House("Rocky Homes","40544 Briarhill Lane","kingston Real estate","Ohio","OH","044503","$134,000","Lakefront property","https://www.bellacollina.com/hubfs/Real%20Estate/Custom%20Built%20Homes.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("KESQL Homes","40544 Beverly Avenue","Nasq Real estate","Clington","NJ","044503","$341,000","Lakefront property","https://nelson-homes.com/media/images/Aries_prefab_homes_modular_homes.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("Lake Homes","40544 Bri st","Berlin Real estate","Ohio","OH","044503","$134,000","Lakefront property","https://nelson-homes.com/media/images/Mensa_house_plan_prefab_homes_mo.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("Lakese Homes","40544 hill st","Atlas Real estate","Ohio","OH","044503","$134,000","Lakefront property","https://nelson-homes.com/media/images/Preseus_prefab_homes_modular_hom.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("Nalsa Homes","40544 arhill st","Benja Real estate","Washington","NYC","044503","$134,000","Lakefront property","https://nelson-homes.com/media/images/Sylvan_prefab_homes_modular_home.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("ASla Homes","40544 Brhill st","Kirlse Real estate","Boston","Ma","044503","$134,000","Lakefront property","https://nelson-homes.com/media/images/Vermillion_prefab_homes_modular_.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("Derva Homes","40544 Briall st","Alss Real estate","Ohio","OH","044503","$134,000","Lakefront property","https://nelson-homes.com/media/images/McKinley_prefab_homes_modular_ho.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
    House("Rcey Homes","40544 Rire st","kingston Real estate","Boston","MA","044503","$134,000","Lakefront property","https://nelson-homes.com/media/images/Bayfield_prefab_homes_modular_ho.2e16d0ba.fill-1920x1080.jpg","2 bedrooms","1","70 sqft","23/06/2023"),
]

class HouseList(TemplateView):
    template_name = "house_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["house"] = house
        return context
