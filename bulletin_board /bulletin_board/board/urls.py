from django.urls import path
from .views import AdList, AdDetail, AdCreate, AdUpdate, AdDelete

urlpatterns = [
    path('', AdList.as_view()),
    path('<int:pk>', AdDetail.as_view(), name='ad'),
    path('add/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/edit/', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),

    ]
