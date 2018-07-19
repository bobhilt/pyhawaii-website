from django.conf.urls import include, url

from django.contrib import admin


urlpatterns = (
    url(r'^admin/', admin.site.urls),

    url(r'^_ah/queue/', include('tasks.urls', namespace='queue')),
    url(r'^_ah/', include('djangae.urls')),

    # insert catch-all rule here
    # url(r'^', ...),
)
