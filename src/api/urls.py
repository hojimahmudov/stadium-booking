from django.urls import path, include
from api.v1 import urls as v1_urls

urlpatterns = [
    path('v1/', include(v1_urls)),
    # path('v2/', include())
]
