from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registration/$', views.RegistrationView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^triangle/$', views.TriangleAPIView.as_view()),
    url(r'^triangle/(?P<pk>\d+)/$', views.TriangleAPIView.as_view()),
    url(r'^square/$', views.SquareAPIView.as_view()),
    url(r'^square/(?P<pk>\d+)/$', views.SquareAPIView.as_view()),
    url(r'^rectangle/$', views.RectangleAPIView.as_view()),
    url(r'^rectangle/(?P<pk>\d+)/$', views.RectangleAPIView.as_view()),
    url(r'^diamond/$', views.DiamondAPIView.as_view()),
    url(r'^diamond/(?P<pk>\d+)/$', views.DiamondAPIView.as_view()),
]