from rest_framework import serializers
from .models import Student,Product,Course,Profile

def name_length(value):
   # if len(value) < 4 :
   if not value.isalpha():
       # raise serializers.ValidationError("Name is too short")
       raise serializers.ValidationError("Name should contain strings")
   elif len(value) < 4:
       raise serializers.ValidationError("Name is too short")
   else:
       return value

def validate_age(value):
    if value < 18 or value > 65:
        raise serializers.ValidationError("Age must be between 18 and 65")

def validate_city(value):
    if not value.islower():
        raise serializers.ValidationError("City name must be in lowercase letters!")

class CourseSerializer(serializers.Serializer):
    course_code = serializers.IntegerField()
    course_name = serializers.CharField()

    def create(self,validated_data):
        return Course.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.sub_code=validated_data.get('course_code',instance.course_code)
        instance.sub_name=validated_data.get('course_name',instance.course_name)

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[name_length])
    age=serializers.IntegerField(validators=[validate_age])
    city=serializers.CharField(validators=[validate_city])
    courses=CourseSerializer(many=True)

    def create(self,validated_data):
        courses_data=validated_data.pop('courses')
        student = Student.objects.create(**validated_data)
        for course_data in courses_data:
            course,created=Course.objects.get_or_create(**course_data)
            student.courses.add(course)
            return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.city= validated_data.get('city',instance.city)
        instance.save()

        return instance

def name_length(value):
    if len(value) < 5 :
        raise serializers.ValidationError("Name is too short")

def validate_price(value):
    if value < 10000 or value >30000:
        raise serializers.ValidationError("Price must be between 10000 and 30000")


def validate_description(value):
    if not value.islower():
       raise serializers.ValidationError("description name must be in lowercase letters!")


class ProductSerializer(serializers.Serializer):
    name=serializers.CharField(validators=[name_length])
    price=serializers.IntegerField(validators=[validate_price])
    description=serializers.CharField(validators=[validate_description])

    def create(self,validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.description= validated_data.get('description',instance.description)
        instance.save()

        return instance
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name','email','phone']

from .models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'