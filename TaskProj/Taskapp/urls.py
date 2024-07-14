
from django.urls import path,include
from .views import *
from.views import StudentAPIAV,StudentDetailAV
from rest_framework .routers import DefaultRouter
from.views import ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()
router.register(r'profile',ProfileViewSet,basename='profile')

urlpatterns = [
    path('idx',index),
    path('home',homepage),
    path('html',htmlpage),
    path('profile/str:name',profile),
    path('temp',DataTemplate),
    path('list',StudentDisplay),
    path('Web',Webpage),
    path('send_email',send_email_view),
    path('test-mail',send_test_email),
    # path('contact',contact_view),
    # path('create',create_profile),
    path('mail-form',mail_form),
    path('api',student_api),
     path('stu-detail/<int:pk>',student_detail),
    # path('update/<int:pk>',partial_update_data),
    path('product_api',product_api),
    # path('pro-detail/<int:pk>',product_detail),
    path('class-api',StudentAPIAV.as_view()),
    path('detail/<int:pk>',StudentDetailAV.as_view()),
    path('',include(router.urls)),
    path('api-token-auth/',obtain_auth_token,name='api_token_auth'),
    path('api/obtain',TokenObtainPairView.as_view()),
    path('api/refresh',TokenRefreshView.as_view()),
    path('api/verify',TokenVerifyView.as_view()),
    path('emp-api',employee_api,name='emp-api'),
    path('emp-list',EmployeeListCreateView.as_view()),
    path('emp-detail/<int:pk>',EmployeeDetaView.as_view()),
    path('emp-mixins-list',EmployeeListCreateMixins.as_view()),
    path('emp-mixins-detail/<int:pk>',EmployeeDetailMixin.as_view())
]