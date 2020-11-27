from django.urls import path
from . import views
# from .views import UpdateView
# from django.views.generic.edit import UpdateView

urlpatterns = [
    path('', views.home, name='home'),
    
    path('update/<int:id>/',  views.update_emp, name='update_emp'),
    path('delete/<int:id>/',  views.delete_emp, name='delete_emp'),

    path('add_emp/',views.add_emp, name='add_emp'),
    path('all_emp/',views.all_emp, name='all_emp'),
    path('add_emp_submission/',views.add_emp_submission, name='add_emp_submission'),
]
