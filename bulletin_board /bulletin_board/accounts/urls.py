from django.urls import path
from .views import BBLoginView, BBLogoutView, RegisterUserView, RegisterDoneView

urlpatterns = [
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done')
]
