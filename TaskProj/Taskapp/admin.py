from django.contrib import admin
from .models import Product,Student
from .models import*
# Register your models here.
admin.site.register(Product)

##one-to-one relationship examples
admin.site.register(Place)
admin.site.register(Restaurant)

admin.site.register(Brand)
admin.site.register(CarModel)

admin.site.register(Student)
admin.site.register(Course)