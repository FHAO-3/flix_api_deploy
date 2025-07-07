from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# 'TokenObtainPairView' é uma view que permite obter um par de tokens JWT (access e refresh)
# 'token_refresh' é uma classe usada para atualizar o token JWT
# 'token_verify' é uma classe usada para verificar a validade do token JWT

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
