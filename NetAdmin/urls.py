from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static

from NetAdmin import views as NetAdmin_views
from MyMessage import views as MyMessage_views

from TA import urls as ta_urls
from Student import urls as student_urls
from Account import urls as account_urls
from Parents import urls as parents_urls
from Agent import urls as admin_urls
import settings

urlpatterns = [
    url(r'^$', NetAdmin_views.landing_page_view),
    url(r'^index/', NetAdmin_views.index_page_view),

    url(r'^account/', include(account_urls)),

    url(r'^student/', include(student_urls)),
    url(r'^parents/', include(parents_urls)),
    url(r'^agent/', include(admin_urls)),
    url(r'^ta/', include(ta_urls)),

    url(r'newmessage/$', MyMessage_views.compose_message_view),
    url(r'^sendmessage/$', MyMessage_views.send_message_view),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^files_list$', NetAdmin_views.files_list),
    url(r'^download/(?P<file_name>.+)$', NetAdmin_views.download),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)