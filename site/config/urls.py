from django.conf.urls import include
from django.conf.urls import url

from django.contrib import admin


urlpatterns = (
    url(r'^admin/', admin.site.urls),

    url(r'^_ah/queue/', include('tasks.urls', namespace='queue')),

    url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
    url(r'^auth/', include('social_django.urls', namespace='social')),

    # insert catch-all rule here
    # url(r'^', ...),
)
