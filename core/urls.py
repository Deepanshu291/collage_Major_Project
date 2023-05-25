from django.urls import path , include
from core.views import *

urlpatterns = [
    path('', home, name="home"),
    path('scan/', scan, name='scan_face'),
    path('attendance/', attendance, name='attendance'),
    path('display/', display, name='display'),
    path('addstudent/', addstudent,name='addstd')
]