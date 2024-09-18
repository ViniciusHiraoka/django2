from django.urls import path
from .views import bemvindo, contato, produto

urlpatterns = [
    path('', bemvindo, name='bemvindo'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto')
]