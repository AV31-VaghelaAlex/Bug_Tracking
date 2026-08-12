
from django.urls import path
from . import views

urlpatterns=[
path('',views.dashboard,name='dashboard'),
path('create/',views.create_bug,name='create_bug'),
path('bug/<int:pk>/',views.bug_detail,name='bug_detail'),
path('my-bugs/',views.my_bugs,name='my_bugs'),
]
