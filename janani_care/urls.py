from django.conf.urls import url, include
from django.contrib import admin
# Static helper function only for development!
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('educational_need.urls')),
    url(r'^account/', include('account.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
