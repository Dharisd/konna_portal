from django.urls import path

from .views import IndexView,PermitCreate,DetailView,PendingView,RejectedView

app_name= "dig_permit"
urlpatterns = [
    path('', IndexView.as_view(), name='index',),
    path('pending/', PendingView.as_view(), name='pending',),
    path('rejected/', RejectedView.as_view(), name='rejected',),
    path('details/<int:pk>/',DetailView.as_view(),name='details'),
    path('create/',PermitCreate.as_view(),name="create")

]