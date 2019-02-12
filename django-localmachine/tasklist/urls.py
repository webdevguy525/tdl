from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
admin.autodiscover()

urlpatterns=[
    url(r'^$', RedirectView.as_view(url='tasks/'), name='home'),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
]
