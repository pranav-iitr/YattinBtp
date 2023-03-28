from .views import Summer ,Winter
from django.urls import path

urlpatterns = [
    path('summer', Summer, name='Summer'),
    path('winter', Winter, name='Winter'),
]