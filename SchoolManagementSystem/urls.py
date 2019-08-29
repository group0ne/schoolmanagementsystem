from django.conf import settings
from django.conf.urls import url
from django.contrib import admin  # THIS LINE
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include

from SchoolManagementSystem import views as core_views
from SchoolManagementSystem.views import home2

admin.autodiscover()

urlpatterns = [
    url(r'^$',home2,name='home2'),
    url(r'^admin/',  admin.site.urls),
    url(r'^home/$', core_views.home, name='home'),
    url(r'^lecturer/', include("Lecturer.urls")),
    url(r'^about/$', core_views.about, name='about'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^signup_staff/$', core_views.signup_staff, name='staff_signup'),
    url(r'^login/$', core_views.user_login, name='login'),
    url(r'^logout/$', core_views.logout_view, name='logout'),
    url(r'^about/$', core_views.about, name='about'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

