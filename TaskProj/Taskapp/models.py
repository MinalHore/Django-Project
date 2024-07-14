from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_code=models.IntegerField()
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=10)
    courses=models.ManyToManyField(Course,related_name='students')

    def __str__(self):
        return f'Students Name is{self.name} and he belongs to {self.city}'


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"

class Restaurant(models.Model):
    restaurant_name=models.CharField(max_length=100)
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return f"Restaurant name is {self.restaurant_name} and located at {self.place}"

class Brand(models.Model):
    brand_name=models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name



class CarModel(models.Model):
    car_name=models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
       return f"Car Name is {self.car_name} and brand is {self.brand}"
class Profile(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.full_name

class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Car(models.Model):
    make=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    year=models.PositiveIntegerField()
    mileage=models.FloatField()

    def __str__(self):
        return f"{self.year}{self.make}{self.model}"
