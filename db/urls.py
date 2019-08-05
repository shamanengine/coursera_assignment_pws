from django.conf.urls import url

from db import views

urlpatterns = [
    url(r'^create/$', views.create),

    url(r'^edit_all/$', views.edit_all),
    url(r'^edit_u1_u2/$', views.edit_u1_u2),

    url(r'^delete_u1/$', views.delete_u1),
    url(r'^unsubscribe_u2_from_blogs/$', views.unsubscribe_u2_from_blogs),

    url(r'^get_topic_created_grated/$', views.get_topic_created_grated),
    url(r'^get_topic_title_ended/$', views.get_topic_title_ended),

    url(r'^get_user_with_limit/$', views.get_user_with_limit),
    url(r'^get_topic_count/$', views.get_topic_count),
    url(r'^get_avg_topic_count/$', views.get_avg_topic_count),

    url(r'^get_blog_that_have_more_than_one_topic/$', views.get_blog_that_have_more_than_one_topic),
    url(r'^get_topic_by_u1/$', views.get_topic_by_u1),
    url(r'^get_user_that_dont_have_blog/$', views.get_user_that_dont_have_blog),

    url(r'^get_topic_that_like_all_users/$', views.get_topic_that_like_all_users),
    url(r'^get_topic_that_dont_have_like/$', views.get_topic_that_dont_have_like),
    url(r'^delete_all/$', views.delete_all),
]
