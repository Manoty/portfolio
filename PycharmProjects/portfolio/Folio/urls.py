from django.urls import path
from . import views as my_views


app_name = 'Folio'
urlpatterns = [
    path('', my_views.index, name='index'),

]


