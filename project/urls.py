from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings 


from main import views

from django.views.generic.base import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^signup/$', 'main.views.sign_up'),
    url(r'^login/$', 'main.views.login_view'),
    url(r'^logout/$', 'main.views.logout_view'),

    url(r'^profile/$', 'main.views.profile_page'),
    url(r'^edit_profile/$', 'main.views.edit_profile'),

    url(r'^create_apartment/$', 'main.views.create_apartment'),
    url(r'^edit_apartment/(?P<pk>.+)/$', 'main.views.edit_apartment'),

    url(r'^apartment_detail/(?P<pk>.+)/$', 'main.views.apartment_detail'),
    url(r'^list_view/$', 'main.views.list_view'),
    url(r'^search/$', 'main.views.ajax_search'),
    url(r'^json_response/$', 'main.views.json_response'),

    url(r'^homepage/$', 'main.views.homepage'),
    url(r'^search_view/$', 'main.views.search_view'),

    #email
    url(r'^sendmail/$', 'main.views.sendmail'),
    url(r'^thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    url(r'^email/$', TemplateView.as_view(template_name='email.html'), name='email'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

