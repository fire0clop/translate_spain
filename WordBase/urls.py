from django.urls import path,include
from .views import mainbase, ListBaseView, CreateBaseView, DetailBaseView, DeleteBaseView, UpdateBaseView
urlpatterns = [
    path('', mainbase, name = 'main_base'),
    path('listbase/', ListBaseView.as_view(), name = 'list_base'),
    path('createword/', CreateBaseView.as_view(), name = 'create_base'),
    path('detail/<int:pk>/', DetailBaseView.as_view(), name = 'detail_word'),
    path('detail/<int:pk>/delete/', DeleteBaseView.as_view(), name = 'delete_word'),
    path('detail/<int:pk>/update', UpdateBaseView.as_view(), name = 'update_word')
]