from django.urls import path, include, re_path
from .views import animal_list, animal_detail
from rest_framework.documentation import include_docs_urls

app_name = "animaldb"
urlpatterns = [
    path('', animal_list, name="animal_list"),
    re_path(r'^(?P<slug>[\w-]+)/$',animal_detail, name="animal_detail"),

    path('docs/', include_docs_urls(title='My API title'))
    
]

