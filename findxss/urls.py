from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='index'),
	path('42/', views.firstchallenge, name='firstchallenge'),
	# path('1337', views.testargument, name='testargument'),
]