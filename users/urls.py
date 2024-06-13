from django.urls import path

from users import views

urlpatterns = [
    path("users/create/", views.CreateUserView.as_view()),
    path("users/list", views.UserList.as_view()),
    path("users/<int:pk>/", views.RetriveUpdateUserView.as_view()),
    path("users/", views.RetriveUpdateUserView.as_view()),
    path('user/<int:pk>/', views.UserDeleteView.as_view()),
    path('token/', views.CreateTokenView.as_view()),
    path('token/refresh/', views.CreateTokenView.as_view()),
]
