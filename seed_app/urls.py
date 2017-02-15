from django.conf.urls import url

from seed_app import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about', views.RegisterView.as_view(), name='about'),
    url(r'^welcome', views.WelcomeView.as_view(), name='welcome'),]