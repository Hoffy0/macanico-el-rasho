from django.urls import path
from .views import Login, DashBoardList, DashBoardDetail, DashBoardCreate, DashBoardUpdate


urlpatterns = [
    path('', Login.as_view(), name="index"),
    path('home/',           DashBoardList.as_view(),   name="home"),
    path('detail/<int:pk>', DashBoardDetail.as_view(), name="reparacion"),
    path('add/',            DashBoardCreate.as_view(), name="crear"),
    path('update/<int:pk>', DashBoardUpdate.as_view(), name="update"),
]
