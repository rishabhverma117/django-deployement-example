from django.conf.urls import url
from mapp import views

#template tagging
app_name = 'mapp'

urlpatterns= [
    url(r'^register/$',views.register,name='register'),
    url(r'login/$',views.user_login,name='user_login'),

]
