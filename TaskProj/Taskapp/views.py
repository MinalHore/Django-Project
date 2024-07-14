from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status





# Create your views here.
def index(request):
    return HttpResponse( 'This is Django Project Running')
def homepage(request):
    return HttpResponse('This is HomePage...')

def htmlpage(request):
    return render(request,'home.html')
def profile(request,name):
    return HttpResponse(f'your profile name is:{name}')

def DataTemplate(request):
    data ='Python is a programming language'
    return render(request,'about.html',{'data':data})

def StudentDisplay(request):
    data=Student.objects.all()
    return render(request,'StudentList.html',{'data':data})

def Webpage(request):
    return render(request,'index.html')

def send_email_view(request):
    if request.method=='POST':
        subject = request.POST.get('subject','Default Subject')
        message = request.POST.get('message','Default Message')
        recipient = request.POST.get('recipient@gmail.com')

        send_mail(
            subject,
            message,
            settings.DEFAULT_FORM_EMAIL,[recipient]

        )
        return HttpResponse('Email Sent Successfully!')
    return render(request,'send_email_html')

def send_test_email(request):
    subject ='Test Email'
    message ='This is a Test email'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=['minalhore659@gmail.com']

    send_mail(
        subject,
        message,
        from_email,
        recipient_list
    )
    return HttpResponse('Test email sent successfully')


# def contact_view(request):
#     if request.method=='POST':
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Your Data has been')

def mail_form(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = f'Message from {name}'

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return HttpResponse("Email sent successfully")
        except Exception as e :
            return HttpResponse(f"Failed to send email:{e}")
    return render(request,'email.html')

from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def student_api(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def student_detail(request,pk):
    if request.method == 'GET':
     stu = Student.objects.get(pk=pk)
     serializer = StudentSerializer(stu)
     return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response('Student Data deleted')
#
# @api_view(['GET','PATCH'])
# def partial_update_data(request,pk):
#     try:
#         stu = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response('Data not found')
#
#     if request.method =='GET':
#         stu = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)
#
#     if request.method =='PATCH':
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import  IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def product_api(request):
    if request.method == 'GET':
        pro=Product.objects.all()
        serializer=ProductSerializer(pro,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    if request.method == 'GET':
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro)
        return Response(serializer.data)

    if request.method == 'PUT':
        pro = Product.objects.get(pk=pk)
        serializer = ProductSerializer(pro,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        pro = Product.objects.get(pk=pk)
        pro.delete()
        return Response('Product Data deleted')

from rest_framework.views import APIView
from.models import Student
from.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

class StudentAPIAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(selfself,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(selfself,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


from django.http import Http404

class StudentDetailAV(APIView):
    permission_classes = [IsAdminUser]

    def get_object(selfself,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        stu=self.get_object(pk=pk)
        serializer=StudentSerializer(stu)
        return Response(serializer.data)

    def put(selfself,request,pk):
        stu=self.get_object(pk=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(selfself,request,pk):
        stu=self.get_object(pk=pk)
        stu.delete()
        return Response('Data deleted successfully')


from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(selfself,request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def retrieve(selfself,request,pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


    def update(selfself,request,pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(selfself,request,pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET','POST'])
def employee_api(request):
    if request.method == 'GET':
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method =='POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return  Response(serializer.errors)


from rest_framework import generics,mixins
from rest_framework import status
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        self.create(request,*args,**kwargs)


class EmployeeListCreateMixins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeDetailMixin(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


