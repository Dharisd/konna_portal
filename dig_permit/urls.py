from django.urls import path

from .views import IndexView,PermitCreate,DetailView

app_name= "dig_permit"
urlpatterns = [
    path('', IndexView.as_view(), name='index',),
    path('details/<int:pk>/',DetailView.as_view(),name='details'),
    path('create/',PermitCreate.as_view(),name="create")

]