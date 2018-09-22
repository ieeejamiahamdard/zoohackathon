from django.urls import path, include, re_path
from .views import animal_list, animal_detail

app_name = "animaldb"
urlpatterns = [

    path('', animal_list, name="animal_list"),
    re_path(r'^(?P<slug>[\w-]+)/$',animal_detail, name="animal_detail")
    # re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]