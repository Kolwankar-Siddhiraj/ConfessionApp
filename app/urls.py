from django.urls import path
from .views import *

urlpatterns = [
    path('', HandleConfession.as_view(), name="confession"),
]



