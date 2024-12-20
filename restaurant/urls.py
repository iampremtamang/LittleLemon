from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include

from .views import *

router = routers.DefaultRouter()
router.register('registration', UserViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', home, name='home'), #home page
    path('api/', include([
        path('', include(router.urls)),
        path('auth/token/', obtain_auth_token),
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.authtoken')),
        path('menu/', MenuView.as_view()),
    ])),
    

]
