from django.urls import path
from .views import *

urlpatterns = [
   path('register/', RegisterView.as_view() ),
   path('shiftget/', ShiftGet.as_view() ),
   path('shiftpost/', ShiftPost.as_view() ),
]