"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import AdditionView
from operation.views import SubtractionView
from operation.views import MultiplicationView
from operation.views import DivisionView
from operation.views import FactorialView
from operation.views import PrimeNumberView
from operation.views import PerfectNumberView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/',AdditionView.as_view()),
    path('subtraction/',SubtractionView.as_view()),
    path('multiply/',MultiplicationView.as_view()),
    path('division/',DivisionView.as_view()),
    path('factorial/',FactorialView.as_view()),
    path('prime/',PrimeNumberView.as_view()),
    path('perfectnumber/',PerfectNumberView.as_view())
]
