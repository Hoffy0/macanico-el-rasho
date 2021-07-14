from django.urls import path
from .views import Login, DashBoardList, DashBoardDetail, DashBoardCreate, DashBoardUpdate, DashBoardDelete
from .views import SliderList, SliderDetail, SliderCreate, SliderUpdate, SliderDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',                 Login.as_view(),                       name="login"),
    path('logout/',          LogoutView.as_view(next_page='index'), name='Logout'),  
    ############################################################################## 
    path('home/',            DashBoardList.as_view(),               name="home"),
    path('detail/<int:pk>',  DashBoardDetail.as_view(),             name="reparacion"),
    path('add/',             DashBoardCreate.as_view(),             name="crear"),
    path('update/<int:pk>/', DashBoardUpdate.as_view(),            name="update"),
    path('delete/<int:pk>/', DashBoardDelete.as_view(),            name="delete"),
    ############################################################################# 
    path('slider/',                 SliderList.as_view(),   name="Sliders"),
    path('slider/detail/<int:pk>/', SliderDetail.as_view(), name="Slider"),
    path('slider/add/',             SliderCreate.as_view(), name="cSlider"),
    path('slider/update/<int:pk>',  SliderUpdate.as_view(), name="uSlider"),
    path('slider/delete/<int:pk>',  SliderDelete.as_view(), name="dSlider")
]
