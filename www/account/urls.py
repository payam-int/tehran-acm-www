from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'^register$', views.Register.as_view()),
]
