from django.contrib import admin
from django.urls import path, include

from project_configs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('main_app.urls')),
]

handler400 = views.error_400
handler404 = views.error_404
handler500 = views.error_500

admin.site.site_title = "Alini Flow"
admin.site.site_header = "Alini Flow"
admin.site.index_header = "Welcome to Alini Flow portal"
