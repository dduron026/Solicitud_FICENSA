from django.conf.urls import url
from general import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

	url(r'^$', views.menu_principal, name='menu_principal'),
	url(r'solicitud_1/', views.solicitud_1, name='solicitud_1'),

	url(r'listado_solicitud/', views.listado_solicitud, name='listado_solicitud'),

	url(r'^solicitud_2/(?P<codigo>\d+)$', views.solicitud_2, name='solicitud_2'),
	url(r'^solicitud_3/(?P<codigo>\d+)$', views.solicitud_3, name='solicitud_3'),
	url(r'^solicitud_4/(?P<codigo>\d+)$', views.solicitud_4, name='solicitud_4'),
	url(r'^solicitud_5/(?P<codigo>\d+)$', views.solicitud_5, name='solicitud_5'),
	
	# 6 ingresar personas dependientes
	url(r'^solicitud_6/(?P<codigo>\d+)/(?P<cantidad>\d+)$', views.solicitud_6, name='solicitud_6'),
	# 7 REFERENCIAS
	url(r'^solicitud_7/(?P<codigo>\d+)$', views.solicitud_7, name='solicitud_7'),
	url(r'^solicitud_8/(?P<codigo>\d+)$', views.solicitud_8, name='solicitud_8'),
	
	# 9 BENEFICIARIOS
	url(r'^solicitud_9/(?P<codigo>\d+)$', views.solicitud_9, name='solicitud_9'),

	# EDITAR
	url(r'^editar_1/(?P<codigo>\d+)$', views.editar_1, name='editar_1'),
	url(r'^editar_2/(?P<codigo>\d+)$', views.editar_2, name='editar_2'),
	url(r'^editar_3/(?P<codigo>\d+)$', views.editar_3, name='editar_3'),
	url(r'^editar_4/(?P<codigo>\d+)$', views.editar_4, name='editar_4'),
	url(r'^editar_5/(?P<codigo>\d+)$', views.editar_5, name='editar_5'),
	
	url(r'^editar_6/(?P<codigo>\d+)/(?P<cantidad>\d+)$', views.editar_6, name='editar_6'),

	url(r'^editar_7/(?P<codigo>\d+)$', views.editar_7, name='editar_7'),
	url(r'^editar_8/(?P<codigo>\d+)$', views.editar_8, name='editar_8'),
	url(r'^editar_9/(?P<codigo>\d+)$', views.editar_9, name='editar_9'),



]