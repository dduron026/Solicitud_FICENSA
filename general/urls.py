from django.conf.urls import url
from general import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

	url(r'^$', views.menu_principal, name='menu_principal'),
	url(r'solicitud_1/', views.solicitud_1, name='solicitud_1'),
	url(r'solicitud_2/', views.solicitud_2, name='solicitud_2'),
	url(r'solicitud_3/', views.solicitud_3, name='solicitud_3'),
	url(r'solicitud_4/', views.solicitud_4, name='solicitud_4'),
	url(r'solicitud_5/', views.solicitud_5, name='solicitud_5'),
	# 6 ingresar personas dependientes
	url(r'solicitud_6/', views.solicitud_6, name='solicitud_6'),
	# 7 REFERENCIAS
	url(r'solicitud_7/', views.solicitud_7, name='solicitud_7'),
	url(r'solicitud_8/', views.solicitud_8, name='solicitud_8'),
	# 9 BENEFICIARIOS
	url(r'solicitud_9/', views.solicitud_9, name='solicitud_9'),


]