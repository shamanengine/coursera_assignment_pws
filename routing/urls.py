# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     url(r'^routing/simple_route/$', views.simple_route),
#     url(r'^routing/slug_route/(?P<slug>[\w\-]{1,16})/$', views.slug_route),
#     url(r'^routing/sum_route/(?P<n>\-?\d+)/(?P<m>\-?\d+)/$', views.sum_route),
#     url(r'^routing/sum_get_method/$', views.sum_get_method),
#     url(r'^routing/sum_post_method/$', views.sum_post_method),
# ]
#

from django.conf.urls import url

from routing.views import (
    simple_route, slug_route, sum_route,
    sum_get_method, sum_post_method,
)

urlpatterns = [
    url(r'^simple_route/$', simple_route),
    url(r'^slug_route/([a-z0-9-_]{1,16})/$', slug_route),
    url(r'^sum_route/(-?\d+)/(-?\d+)/$', sum_route),
    url(r'^sum_get_method/$', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method),
]
