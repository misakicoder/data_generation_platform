"""Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from User.views import *
from Task.views import *
from Data.views import *
from Model.views import *
from Algorithm.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    #User
    path("login/", login.as_view(), name="login"),
    path("verify_code/", send_verification_code.as_view(), name="verify_code"),
    #Task
    path("tasks/", tasks.as_view(), name="tasks"),
    path("task/", task.as_view(), name="task"),
    path("data_manager/",data_manager.as_view(), name="data_manager"),
    #Data
    path("data/", data.as_view(), name="data"),
    path("ori_data/", ori_data.as_view(), name="ori_data"),
    path("data_cols/",data_cols.as_view(),name="data_cols"),
    path("cleaned_data/", cleaned_data.as_view(), name="cleaned_data"),
    path("marked_data/", marked_data.as_view(), name="marked_data"),
    path("preprocessed_data/", preprocessed_data.as_view(), name="preprocessed_data"),
    path("marked_preprocessed_data/", marked_preprocessed_data.as_view(), name="marked_preprocessed_data"),
    path("result/", result.as_view(), name="result"),
    path("result_zip/", result_zip.as_view(), name="result_zip"),
    #Algorithm
    path("algorithms/", algorithms.as_view(), name="algorithms"),
    #Model
    path("models/", models.as_view(), name="models"),
]

