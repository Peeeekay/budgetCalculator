from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
from hello.budgetView import BudgetView
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^test',hello.views.getData, name='getData'),
    url(r'^webhook',BudgetView.as_view(), name='budget'),
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]