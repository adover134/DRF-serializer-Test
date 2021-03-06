"""webPages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from webPages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signupPage/', views.signupPage, name='signupPage'),
    path('signup/', views.signup, name='signup'),
    path('infoCheck/', views.infoCheck, name='infoCheck'),
    path('normalUserReviewSearch/', views.normal_user_review_search, name='normalUserReviewSearch'),
    path('normal_user_review_read/', views.normal_user_review_read, name='normalUserReviewRead'),
    path('toggleRecommmend/', views.normal_user_review_recommend, name='normalUserReviewRecommend'),
    path('toggleReport/', views.normal_user_review_report, name='normalUserReviewReport'),
    path('db/', include('DBs.urls')),
    path('test/', include('webTests.urls'))
]
