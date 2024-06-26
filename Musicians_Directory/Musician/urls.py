from django.urls import path
from . import views 
urlpatterns = [
    path('add/',views.add_musician , name= 'add_musician'),
    path('del/<int:id>',views.delete_musician, name ='delete_musician'),
    path('edit/<int:id>',views.edit_musician, name ='edit_musician'),
    
    
]