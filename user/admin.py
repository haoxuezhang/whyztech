from django.contrib import admin
# from .models import Important, Solutions, Products, Example, News, Aboutus, UserProfile, SolutionCate, ProductCate, NewsCate
from .models import Products, ProductSecondCate, ProductMainCate, ApplicationCate, Brands, News, AboutUs

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductSecondCate)
admin.site.register(ProductMainCate)
admin.site.register(ApplicationCate)
admin.site.register(Brands)
admin.site.register(News)
admin.site.register(AboutUs)
