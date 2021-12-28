from django.conf.urls import url
from . import views
from django.urls.conf import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    path('neighborhood/<int:neighborhood_id>/',views.neighborhood,name='neighborhood'),
    path('neighborhood',views.neighborhood,name='neighborhood'),
    path('business/<int:neighborhood_id>/',views.business,name='business'),
    path('choose_neighborhood/<int:neighborhood_id>/',views.join_neighborhood,name='choose_neighborhood'),
    path('leave_neighborhood/<int:neighborhood_id>/',views.leave_neighborhood,name='leave_neighborhood'),
    path('post/<int:neighborhood_id>/',views.post,name='post'),
    path('delete_business/<business_id>',views.delete_business,name='delete_business'),
    path('update_business/<business_id>',views.update_business,name='update_business'),
    path('delete_post/<post_id>',views.delete_post,name='delete_post'),
    path('update_post/<post_id>',views.update_post,name='update_post'),
    path('update_neighborhood/<neighborhood_id>',views.update_neighborhood,name='update_neighborhood'),
    path('delete_neighborhood/<neighborhood_id>',views.delete_neighborhood,name='delete_neighborhood'),
    path('users/<pk>',views.users_profile,name='users_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)