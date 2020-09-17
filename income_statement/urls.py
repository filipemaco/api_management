from django.urls import include, path

from .views import (IncomeStatementDetail, IncomeStatementList)


urlpatterns = [
    path('<int:pk>/', IncomeStatementDetail.as_view()),
    path('', IncomeStatementList.as_view()),
]
