from django.conf.urls import include
from django.conf.urls import url

from django.contrib import admin


urlpatterns = (
    url(r'^admin/', admin.site.urls),

    url(r'^_ah/queue/', include('tasks.urls', namespace='queue')),
    url(r'^_ah/', include('djangae.urls')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # insert catch-all rule here
    # url(r'^', ...),
)
