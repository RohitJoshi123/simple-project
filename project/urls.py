from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Define custom view for 404 error
handler404 = "djangoproject.views.my_custom_404_view"
# Define custom view for 500 error
# handler500 = "djangoproject.views.my_custom_500_view"

urlpatterns = patterns('',
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
