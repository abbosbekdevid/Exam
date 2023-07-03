from django.urls import path
from .views import (AllBookGetView,DeleteBookApiView,CreateBookApiView,UpdateBookApiView)
urlpatterns = [
    path('', AllBookGetView.as_view()),
    path('create/',CreateBookApiView.as_view()),
    path('category/update/<int:id>/',UpdateBookApiView.as_view()),
    path('category/delete/<int:id>/',DeleteBookApiView.as_view()),
]

