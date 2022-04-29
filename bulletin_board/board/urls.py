from django.urls import path
from .views import AdList, AdDetail, AdCreate, AdUpdate, AdDelete, ResponseList, \
    ResponseCreate, ResponseDelete, CategoryView, ReactionView, accept_response


urlpatterns = [
    path('', AdList.as_view()),
    path('<int:pk>', AdDetail.as_view(), name='ad'),
    path('add/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/edit/', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
    path('<int:pk>/response/', ResponseCreate.as_view(), name='response'),
    path('reaction/', ReactionView.as_view(), name='reaction_to_response'),
    path('profile/', ResponseList.as_view(), name='profile'),
    path('profile/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete'),
    path('category/<int:cat>/', CategoryView.as_view(), name='ads_category'),
    path('profile/<int:pk>/accept/', accept_response, name='response_accept'),
    ]
