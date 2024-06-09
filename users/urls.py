from django.urls import path

from users import views

urlpatterns = [
    path("users/create/", views.CreateUserView.as_view()),
    # listar usando el verbo GET y actualizar usando el verbo UPDATE
    path("users/", views.RetriveUpdateUserView.as_view()),
    path('user/<int:pk>/', views.UserDeleteView.as_view()),
    path('token/', views.CreateTokenView.as_view()),
    path('token/refresh/', views.CreateTokenView.as_view()),
]
