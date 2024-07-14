# from django.test import TestCase
# from .models import Employee
# # Create your tests here.
#
# class EmployeeModelTest(TestCase):
#     pass
#
#     def setUp(self):
#         # Create sample data of employee for testing
#         self.employee=Employee.objects.create(
#             name='Aniket Thakur',
#             age=20,
#             city='Bhopal'
#         )
#     #test if the employee object or instance was created correctly or not
#     def test_employee_creation(self):
#         self.assertEqual(self.employee.name,'Aniket Thakur')
#         self.assertEqual(self.employee.age, 20)
#         self.assertEqual(self.employee.city,'Bhopal')
#
#     def test_employee_update(self):
#         self.employee.name='Pratik Mrunal'
#         self.employee.save()
#         self.assertEqual(self.employee.name,'Pratik Mrunal')
#         print('Name after updation:',self.employee.name)
#
#     def test_employee_delete(self):
#         self.employee.delete()
#         print('Name after deletion:',self.employee.name)
#         self.assertEqual(Employee.objects.count(),0)

# import unittest
# class MyTestCase(unittest.TestCase):
#       def test_addition(self):
#           result=10+10
#           self.assertEqual(result,20)
#
#       def test_subtraction(self):
#           result=30-10
#           self.assertEqual(result,20)

from django.urls import reverse
from rest_framework import status
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User

class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='AdminUser',password='123456')
        self.client.login(username='AdminUser',password='123456')
        self.url=reverse('emp-api')

        self.emp1 = Employee.objects.create(name='Kashish',age=21,city='Lucknow')
        self.emp2 = Employee.objects.create(name='Rushali',age=24,city='Rajkot')

    def test_get_employee(self):
        response = self.client.get(self.url)
        emp=Employee.objects.all().values()
        print('Employee Data:',emp)
        serializer = EmployeeSerializer(emp,many=True)
        print('Serializer Data:',serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

    def test_employee_creation(self):
        data={
            'name':'Suresh kumar',
            'age':60,
            'city':'Hyderabad'
        }
        response=self.client.post('/task/emp-api',data=data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        print(response.json())
        response_data=response.json()
        self.assertEqual(response_data['name'],'Suresh kumar')
        self.assertEqual(response_data['age'],60)
        self.assertEqual(response_data['city'],'Hyderabad')


from django.test import TestCase
from .models import Car  # assuming 'myapp' is your Django app name


class CarModelTestCase(TestCase):
    def setUp(self):
        Car.objects.create(make='Toyota', model='Camry', year=2022, mileage=15000.5)

    def test_car_creation(self):
        """Test that a car instance can be created"""
        car = Car.objects.get(make='Toyota')
        self.assertEqual(car.make, 'Toyota')
        self.assertEqual(car.model, 'Camry')
        self.assertEqual(car.year, 2022)
        self.assertAlmostEqual(car.mileage, 15000.5, places=1)


    def test_car_update(self):
        """Test updating a car instance"""
        car=Car.objects.get(make='Toyota')
        car.mileage=16000.2
        car.save()
        updated_car=Car.objects.get(make='Toyota')
        self.assertAlmostEqual(updated_car.mileage,16000.2,places=1)

    def test_car_deletion(self):
        """Test deleting a car instance"""
        car=Car.objects.get(make='Toyota')
        car.delete()
        with self.assertRaises(Car.DoesNotExist):
            Car.objects.get(make='Toyota')

