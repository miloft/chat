from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from accounts.views import ELoginView

urlpatterns = [
    url(r'^login/', ELoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    path('', include('accounts.urls'))
]