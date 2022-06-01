from django.urls import path
from .views import UserView, ReadUpdateDelet


urlpatterns=[
    path('',UserView.as_view() ),
    path('/<int:pk>', ReadUpdateDelet.as_view())
]
