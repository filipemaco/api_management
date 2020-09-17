from django.urls import include, path

from .views import (CustomUserDetail, CustomUserList)


urlpatterns = [
    path('<int:pk>/', CustomUserDetail.as_view()),
    path('', CustomUserList.as_view()),
]
