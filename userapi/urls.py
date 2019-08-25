from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from django.conf.urls import url, include
urlpatterns=[
    #url(r'^create/$', CreateUserAPIView.as_view()),
    #path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^userlist/',views.userList.as_view()),
]