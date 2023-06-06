from django.urls import path
from .views import *

urlpatterns = [
    path('',addandshow,name='addandshow'),
    path('update/',update,name='update'),
    path('<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update'),
    path('signup/',signup,name='signup'),
    path('login/',user_login,name='login'),
]
