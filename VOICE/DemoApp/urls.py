from django.urls import path
from . import views


urlpatterns = [
    path('',views.hi1,name='home-page1'),
    path('welc/', views.regis,name='home-reg'),
    path('new/', views.hi,name='home-page11'),
    path('openlog/', views.log,name='home-page12'),
    path('regisopen/', views.openregis,name='home-page13'),
    path('regisemail/', views.emailregis,name='home-page14'),
    path('regissecurity/', views.securityregis,name='home-page15'),
    path('regispasswd/', views.passwdregis,name='home-page16'),
    path('update1/', views.insertdata,name='home-page17'),
    path('pass12/', views.passwd,name='home-page2'),
    path('home123/', views.openhome,name='homePage3'),
    path('home10/', views.last,name='homePage3'),
    path('mai/', views.homepg,name='four'),
    path('val/', views.openvalid,name='four'),
    path('rec1/', views.innercompose,name='five'),
    path('sub1/', views.innersub,name='six'),
    path('bod1/', views.innerbod,name='seven'),
    path('compose123/', views.opencompose,name='home-page4'),
    path('inbox123/', views.openinbox,name='home-page5'),
    path('logout123/', views.openlogout,name='home-page6'),
    path('readinbox/', views.readInbox,name='home-page8'),
    path('speakinbox/', views.speakInbox,name='home-page7'),


]