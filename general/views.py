from django.shortcuts import render, redirect
from django.db import transaction, IntegrityError

# Create your views here.


# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.models import User, Group

from general.forms import *
from .models import * 



def menu_principal(request):
	return render(request, 'menu_principal.html', {})




@transaction.atomic
def solicitud_1(request):
	form = SolicitudForm()
	if request.POST:
		try:
			with transaction.atomic():
				solicitud = Solicitud()
				solicitud.producto = None if request.POST.get('producto') == '' else request.POST.get('producto')
				solicitud.moneda = None if request.POST.get('moneda') == '' else request.POST.get('moneda')
				solicitud.titular = None if request.POST.get('titular') == '' else request.POST.get('titular')
				solicitud.firma = None if request.POST.get('firma') == '' else request.POST.get('firma')
				solicitud.estado = None if request.POST.get('estado') == '' else request.POST.get('estado')
				solicitud.identidad = None if request.POST.get('identidad') == '' else request.POST.get('identidad')
				solicitud.nombre_completo = None if request.POST.get('nombre_completo') == '' else request.POST.get('nombre_completo')
				solicitud.cod_pais_nacimiento = Pais.objects.get(pk=request.POST.get('cod_pais_nacimiento'))
				solicitud.cod_depto_nacimiento = Departamento.objects.get(pk=request.POST.get('cod_depto_nacimiento'))
				solicitud.cod_municipio = Municipio.objects.get(pk=request.POST.get('cod_municipio'))
				solicitud.nacionalidad =  None if request.POST.get('nacionalidad') == '' else request.POST.get('nacionalidad')
				solicitud.lugar_nacimiento = None if request.POST.get('lugar_nacimiento') == '' else request.POST.get('lugar_nacimiento')
				solicitud.estado = 0
				solicitud.cod_vista = 2
				solicitud.save()

				return redirect(reverse('solicitud_2', kwargs={'codigo': solicitud.id_solicitud}))

		except Exception as e:
			mensaje = 'error'

	return render(request, 'solicitud_1.html', {'form': form} )



@transaction.atomic
def solicitud_2(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = SolicitudForm()
	if request.POST:
		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.estado_civil = None if request.POST.get('estado_civil') == '' else request.POST.get('estado_civil')
				solicitud.sexo = None if request.POST.get('sexo') == '' else request.POST.get('sexo')
				solicitud.nombre_conyuge = None if request.POST.get('nombre_conyuge') == '' else request.POST.get('nombre_conyuge')
				solicitud.tipo_identificacion= None if request.POST.get('tipo_identificacion') == '' else request.POST.get('tipo_identificacion')
				solicitud.rtn= None if request.POST.get('rtn') == '' else request.POST.get('rtn')
				solicitud.direccion_detallada= None if request.POST.get('direccion_detallada') == '' else request.POST.get('direccion_detallada')
				solicitud.cod_depto_direccion = Departamento.objects.get(pk=request.POST.get('cod_depto_direccion'))
				solicitud.cod_mun_direccion = Municipio.objects.get(pk=request.POST.get('cod_mun_direccion'))
				solicitud.cod_col_direccion = Colonia.objects.get(pk=request.POST.get('cod_col_direccion'))
				solicitud.referencia = None if request.POST.get('referencia') == '' else request.POST.get('referencia')
				solicitud.casa = None if request.POST.get('casa') == '' else request.POST.get('casa')
				solicitud.telefono_casa = None if request.POST.get('telefono_casa') == '' else request.POST.get('telefono_casa')
				solicitud.cod_vista = 3
				solicitud.save()
				return redirect(reverse('solicitud_3', kwargs={'codigo': solicitud.id_solicitud}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'solicitud_2.html', {'form': form, 'solicitud': solicitud})





@transaction.atomic
def solicitud_3(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = SolicitudForm()
	if request.POST:
		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.telefono2 = None if request.POST.get('telefono2') == '' else request.POST.get('telefono2')
				solicitud.celular = None if request.POST.get('celular') == '' else request.POST.get('celular')
				solicitud.fax = None if request.POST.get('fax') == '' else request.POST.get('fax')
				solicitud.cod_pais_residencia = Pais.objects.get(pk=request.POST.get('cod_pais_residencia'))
				solicitud.nivel_educativo = None if request.POST.get('nivel_educativo') == '' else request.POST.get('nivel_educativo')
				solicitud.correo_electronico = None if request.POST.get('correo_electronico') == '' else request.POST.get('correo_electronico')
				solicitud.profesion = None if request.POST.get('profesion') == '' else request.POST.get('profesion')
				solicitud.cod_actividad_economica = None if request.POST.get('cod_actividad_economica') == '' else request.POST.get('cod_actividad_economica')
				solicitud.cod_depto_direccion_empresa = Departamento.objects.get(pk=request.POST.get('cod_depto_direccion_empresa'))
				solicitud.nombre_empresa = None if request.POST.get('nombre_empresa') == '' else request.POST.get('nombre_empresa')
				solicitud.cod_vista = 4
				
				solicitud.save()
				return redirect(reverse('solicitud_4', kwargs={'codigo': solicitud.id_solicitud}))				
		except Exception as e:
			mensaje = 'error'
	return render(request, 'solicitud_3.html', {'form': form, 'solicitud': solicitud})


@transaction.atomic
def solicitud_4(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = SolicitudForm()
	if request.POST:
		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.cod_mun_direccion_empresa = Municipio.objects.get(pk=request.POST.get('cod_mun_direccion_empresa'))
				solicitud.telefono_empresa = None if request.POST.get('telefono_empresa') == '' else request.POST.get('telefono_empresa')
				solicitud.direccion_detallada_empresa = None if request.POST.get('direccion_detallada_empresa') == '' else request.POST.get('direccion_detallada_empresa')
				solicitud.posicion_empresa = None if request.POST.get('posicion_empresa') == '' else request.POST.get('posicion_empresa')
				solicitud.antiguedad_meses = None if request.POST.get('antiguedad_meses') == '' else request.POST.get('antiguedad_meses')
				solicitud.comerciante_individual = None if request.POST.get('comerciante_individual') == '' else request.POST.get('comerciante_individual')
				solicitud.detalle_o_giro = None if request.POST.get('detalle_o_giro') == '' else request.POST.get('detalle_o_giro')
				solicitud.nivel_ingresos_smmv = None if request.POST.get('nivel_ingresos_smmv') == '' else request.POST.get('nivel_ingresos_smmv')			
				solicitud.cod_vista = 5
				
				solicitud.save()
				return redirect(reverse('solicitud_5', kwargs={'codigo': solicitud.id_solicitud}))				
		except Exception as e:
			mensaje = 'error'

	return render(request, 'solicitud_4.html', {'form': form, 'solicitud': solicitud} )	




@transaction.atomic
def solicitud_5(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = SolicitudForm()
	if request.POST:
		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.cargo_publico = None if request.POST.get('cargo_publico') == '' else request.POST.get('cargo_publico')		
				solicitud.cod_institucion_pub = Institucion.objects.get(pk=request.POST.get('cod_institucion_pub'))		
				solicitud.cant_personas =	None if request.POST.get('cant_personas') == '' else request.POST.get('cant_personas')	
				solicitud.cod_vista = 6		
				solicitud.save()
				return redirect(reverse('solicitud_6', kwargs={'codigo': solicitud.id_solicitud, 'cantidad': solicitud.cant_personas}))					

		except Exception as e:
			raise e


	return render(request, 'solicitud_5.html', {'form': form, 'solicitud': solicitud} )	


# ingresar dependientes
@transaction.atomic
def solicitud_6(request, codigo, cantidad):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = DependienteForm()
	if request.POST:
		try:
			with transaction.atomic():
				nombre_completo = request.POST.getlist('nombre_completo[]')
				parentesco = request.POST.getlist('parentesco[]')
				identidad = request.POST.getlist('identidad[]')
				tipo_id = request.POST.getlist('tipo_id[]')

				counter = 0
				for x in nombre_completo:
					personas = Dependiente()
					solicitud = Solicitud.objects.get(id_solicitud=codigo)
					personas.id_solicitud = Solicitud.objects.get(pk=codigo)
					personas.nombre_completo = None if nombre_completo[counter] == '' else nombre_completo[counter]
					personas.parentesco = None if parentesco[counter] == '' else parentesco[counter]
					personas.identidad = None if identidad[counter] == '' else identidad[counter]
					personas.tipo_id = None if tipo_id[counter] == '' else tipo_id[counter]
					solicitud.cod_vista = 7
					personas.save()
					solicitud.save()
					counter += 1

				return redirect(reverse('solicitud_7', kwargs={'codigo': solicitud.id_solicitud}))	

		except Exception as e:
			mensaje = 'error'
	
	ctx = {
		'form': form,
		'solicitud': solicitud,
		'cantidad': range(0,int(cantidad)),
	}			

	return render(request, 'solicitud_6.html', ctx )	





@transaction.atomic
def solicitud_7(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = ReferenciaForm()
	if request.POST:
		try:
			with transaction.atomic():
				nombre_completo = request.POST.getlist('nombre_completo[]')
				telefono = request.POST.getlist('telefono[]')
				familiar = request.POST.getlist('familiar[]')

				counter = 0

				for x in nombre_completo:
					ref = Referencia()
					solicitud = Solicitud.objects.get(id_solicitud=codigo)
					ref.id_solicitud = solicitud
					ref.nombre_completo = None if nombre_completo[counter] == '' else nombre_completo[counter]
					ref.telefono = None if telefono[counter] == '' else telefono[counter]
					ref.familiar = None if familiar[counter] == '' else familiar[counter]
					solicitud.cod_vista = 8
					ref.save()
					solicitud.save()
					counter += 1


				return redirect(reverse('solicitud_8', kwargs={'codigo': solicitud.id_solicitud}))					
		except Exception as e:
			raise e

	return render(request, 'solicitud_7.html', {'form': form, 'solicitud': solicitud} )	



@transaction.atomic
def solicitud_8(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = SolicitudForm()
	if request.POST:
		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.proposito = None if request.POST.get('proposito') == '' else request.POST.get('proposito')
				solicitud.monto_inicial =  None if request.POST.get('monto_inicial') == '' else request.POST.get('monto_inicial')
				solicitud.origen_deposito =  None if request.POST.get('origen_deposito') == '' else request.POST.get('origen_deposito')
				solicitud.monto_mensual_estimado =  None if request.POST.get('monto_mensual_estimado') == '' else request.POST.get('monto_mensual_estimado')		
				solicitud.cod_vista = 9				
				solicitud.save()
				return redirect(reverse('solicitud_9', kwargs={'codigo': solicitud.id_solicitud}))					

		except Exception as e:
			raise e

	return render(request, 'solicitud_8.html', {'form': form, 'solicitud': solicitud} )	


@transaction.atomic
def solicitud_9(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	form = BeneficiarioForm()
	if request.POST:
		try:
			with transaction.atomic():
				nombre_completo = request.POST.getlist('nombre_completo[]')
				identidad = request.POST.getlist('identidad[]')
				parentesco = request.POST.getlist('parentesco[]')
				tipo_id = request.POST.getlist('tipo_id[]')
				porcentaje = request.POST.getlist('porcentaje[]')

				counter = 0
				for x in nombre_completo:
					beneficiario = Beneficiario()
					solicitud = Solicitud.objects.get(id_solicitud=codigo)
					beneficiario.id_solicitud = solicitud
					beneficiario.nombre_completo = None if nombre_completo[counter] == '' else nombre_completo[counter]
					beneficiario.identidad = None if identidad[counter] == '' else identidad[counter]
					beneficiario.parentesco = None if parentesco[counter] == '' else parentesco[counter]
					beneficiario.tipo_id = None if tipo_id[counter] == '' else tipo_id[counter]
					beneficiario.porcentaje = None if porcentaje[counter] == '' else porcentaje[counter]
					solicitud.estado = 1
					solicitud.cod_vista = 10
					beneficiario.save()
					solicitud.save()
					counter += 1


				return redirect('menu_principal')
		except Exception as e:
			raise e

	return render(request, 'solicitud_9.html', {'form': form, 'solicitud': solicitud} )		



def listado_solicitud(request):
	lista = Solicitud.objects.all().order_by('id_solicitud')

	return render(request, 'listado_solicitud.html', {'lista': lista})	






# ****************************************EDITAR************************************************************** 

@transaction.atomic
def editar_1(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)

		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.producto = None if request.POST.get('producto') == '' else request.POST.get('producto')
				solicitud.moneda = None if request.POST.get('moneda') == '' else request.POST.get('moneda')
				solicitud.titular = None if request.POST.get('titular') == '' else request.POST.get('titular')
				solicitud.firma = None if request.POST.get('firma') == '' else request.POST.get('firma')
				solicitud.estado = None if request.POST.get('estado') == '' else request.POST.get('estado')
				solicitud.identidad = None if request.POST.get('identidad') == '' else request.POST.get('identidad')
				solicitud.nombre_completo = None if request.POST.get('nombre_completo') == '' else request.POST.get('nombre_completo')
				solicitud.cod_pais_nacimiento = Pais.objects.get(pk=request.POST.get('cod_pais_nacimiento'))
				solicitud.cod_depto_nacimiento = Departamento.objects.get(pk=request.POST.get('cod_depto_nacimiento'))
				solicitud.cod_municipio = Municipio.objects.get(pk=request.POST.get('cod_municipio'))
				solicitud.nacionalidad =  None if request.POST.get('nacionalidad') == '' else request.POST.get('nacionalidad')
				solicitud.lugar_nacimiento = None if request.POST.get('lugar_nacimiento') == '' else request.POST.get('lugar_nacimiento')
				solicitud.estado = 0
				solicitud.cod_vista = 2
				solicitud.save()

				return redirect(reverse('editar_2', kwargs={'codigo': solicitud.id_solicitud}))

		except Exception as e:
			mensaje = 'error'

	return render(request, 'editar_1.html', {'form': form} )


@transaction.atomic
def editar_2(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)

		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.estado_civil = None if request.POST.get('estado_civil') == '' else request.POST.get('estado_civil')
				solicitud.sexo = None if request.POST.get('sexo') == '' else request.POST.get('sexo')
				solicitud.nombre_conyuge = None if request.POST.get('nombre_conyuge') == '' else request.POST.get('nombre_conyuge')
				solicitud.tipo_identificacion= None if request.POST.get('tipo_identificacion') == '' else request.POST.get('tipo_identificacion')
				solicitud.rtn= None if request.POST.get('rtn') == '' else request.POST.get('rtn')
				solicitud.direccion_detallada= None if request.POST.get('direccion_detallada') == '' else request.POST.get('direccion_detallada')
				solicitud.cod_depto_direccion = Departamento.objects.get(pk=request.POST.get('cod_depto_direccion'))
				solicitud.cod_mun_direccion = Municipio.objects.get(pk=request.POST.get('cod_mun_direccion'))
				solicitud.cod_col_direccion = Colonia.objects.get(pk=request.POST.get('cod_col_direccion'))
				solicitud.referencia = None if request.POST.get('referencia') == '' else request.POST.get('referencia')
				solicitud.casa = None if request.POST.get('casa') == '' else request.POST.get('casa')
				solicitud.telefono_casa = None if request.POST.get('telefono_casa') == '' else request.POST.get('telefono_casa')
				solicitud.cod_vista = 3
				solicitud.save()	

				return redirect(reverse('editar_3', kwargs={'codigo': solicitud.id_solicitud}))

		except Exception as e:
			mensaje = 'error'

	return render(request, 'editar_2.html', {'form': form, 'solicitud': solicitud} )	



@transaction.atomic
def editar_3(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)

		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.telefono2 = None if request.POST.get('telefono2') == '' else request.POST.get('telefono2')
				solicitud.celular = None if request.POST.get('celular') == '' else request.POST.get('celular')
				solicitud.fax = None if request.POST.get('fax') == '' else request.POST.get('fax')
				solicitud.cod_pais_residencia = Pais.objects.get(pk=request.POST.get('cod_pais_residencia'))
				solicitud.nivel_educativo = None if request.POST.get('nivel_educativo') == '' else request.POST.get('nivel_educativo')
				solicitud.correo_electronico = None if request.POST.get('correo_electronico') == '' else request.POST.get('correo_electronico')
				solicitud.profesion = None if request.POST.get('profesion') == '' else request.POST.get('profesion')
				solicitud.cod_actividad_economica = None if request.POST.get('cod_actividad_economica') == '' else request.POST.get('cod_actividad_economica')
				solicitud.cod_depto_direccion_empresa = Departamento.objects.get(pk=request.POST.get('cod_depto_direccion_empresa'))
				solicitud.nombre_empresa = None if request.POST.get('nombre_empresa') == '' else request.POST.get('nombre_empresa')
				solicitud.cod_vista = 4
				
				solicitud.save()		
				
				return redirect(reverse('editar_4', kwargs={'codigo': solicitud.id_solicitud}))

		except Exception as e:
			mensaje = 'error'

	return render(request, 'editar_3.html', {'form': form, 'solicitud': solicitud} )




@transaction.atomic
def editar_4(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)
		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.cod_mun_direccion_empresa = Municipio.objects.get(pk=request.POST.get('cod_mun_direccion_empresa'))
				solicitud.telefono_empresa = None if request.POST.get('telefono_empresa') == '' else request.POST.get('telefono_empresa')
				solicitud.direccion_detallada_empresa = None if request.POST.get('direccion_detallada_empresa') == '' else request.POST.get('direccion_detallada_empresa')
				solicitud.posicion_empresa = None if request.POST.get('posicion_empresa') == '' else request.POST.get('posicion_empresa')
				solicitud.antiguedad_meses = None if request.POST.get('antiguedad_meses') == '' else request.POST.get('antiguedad_meses')
				solicitud.comerciante_individual = None if request.POST.get('comerciante_individual') == '' else request.POST.get('comerciante_individual')
				solicitud.detalle_o_giro = None if request.POST.get('detalle_o_giro') == '' else request.POST.get('detalle_o_giro')
				solicitud.nivel_ingresos_smmv = None if request.POST.get('nivel_ingresos_smmv') == '' else request.POST.get('nivel_ingresos_smmv')			
				solicitud.cod_vista = 5
				
				solicitud.save()	
				
				return redirect(reverse('editar_5', kwargs={'codigo': solicitud.id_solicitud}))

		except Exception as e:
			mensaje = 'error'

	return render(request, 'editar_4.html', {'form': form, 'solicitud': solicitud} )	


@transaction.atomic
def editar_5(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)
	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)

		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.cargo_publico = None if request.POST.get('cargo_publico') == '' else request.POST.get('cargo_publico')		
				solicitud.cod_institucion_pub = Institucion.objects.get(pk=request.POST.get('cod_institucion_pub'))		
				solicitud.cant_personas =	None if request.POST.get('cant_personas') == '' else request.POST.get('cant_personas')	
				solicitud.cod_vista = 6		
				solicitud.save()
				return redirect(reverse('editar_6', kwargs={'codigo': solicitud.id_solicitud, 'cantidad': solicitud.cant_personas}))					


		except Exception as e:
			mensaje = 'error'

	return render(request, 'editar_5.html', {'form': form, 'solicitud': solicitud} )	



@transaction.atomic
def editar_6(request, codigo, cantidad):
	x = Dependiente.objects.filter(id_solicitud=codigo)
	solicitud = Solicitud.objects.get(pk=codigo)

	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
		dependientes = []
		for dependiente in x:
			dependiente = DependienteForm(instance=dependiente)
			dependientes.append(dependiente)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)	
	
	
		try:
			with transaction.atomic():
				nombre_completo = request.POST.getlist('nombre_completo[]')
				parentesco = request.POST.getlist('parentesco[]')
				identidad = request.POST.getlist('identidad[]')
				tipo_id = request.POST.getlist('tipo_id[]')

				dependiente = Dependiente.objects.filter(id_solicitud=codigo).delete()

				counter = 0
				for x in nombre_completo:
					dependiente = Dependiente()
					solicitud = Solicitud.objects.get(id_solicitud=codigo)
					dependiente.id_solicitud = Solicitud.objects.get(pk=codigo)
					dependiente.nombre_completo = None if nombre_completo[counter] == '' else nombre_completo[counter]
					dependiente.parentesco = None if parentesco[counter] == '' else parentesco[counter]
					dependiente.identidad = None if identidad[counter] == '' else identidad[counter]
					dependiente.tipo_id = None if tipo_id[counter] == '' else tipo_id[counter]
					solicitud.cod_vista = 7
					dependiente.save()
					solicitud.save()
					counter += 1

				return redirect(reverse('editar_7', kwargs={'codigo': solicitud.id_solicitud}))	

		except Exception as e:
			mensaje = 'error'
	
	ctx = {
		'form': form,
		'solicitud': solicitud,
		'dependientes': dependientes,
		'cantidad': range(0,int(cantidad)),
	}			

	return render(request, 'editar_6.html', ctx )



@transaction.atomic
def editar_7(request, codigo):
	x = Referencia.objects.filter(id_solicitud=codigo)
	solicitud = Solicitud.objects.get(pk=codigo)

	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
		referencias = []
		for referencia in x:
			referencia = ReferenciaForm(instance=referencia)
			referencias.append(referencia)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)

		try:
			with transaction.atomic():
				nombre_completo = request.POST.getlist('nombre_completo[]')
				telefono = request.POST.getlist('telefono[]')
				familiar = request.POST.getlist('familiar[]')

				referencia = Referencia.objects.filter(id_solicitud=codigo).delete()
				counter = 0

				for x in nombre_completo:
					referencia = Referencia()
					solicitud = Solicitud.objects.get(id_solicitud=codigo)
					referencia.id_solicitud = solicitud
					referencia.nombre_completo = None if nombre_completo[counter] == '' else nombre_completo[counter]
					referencia.telefono = None if telefono[counter] == '' else telefono[counter]
					referencia.familiar = None if familiar[counter] == '' else familiar[counter]
					solicitud.cod_vista = 8
					referencia.save()
					solicitud.save()
					counter += 1


				return redirect(reverse('editar_8', kwargs={'codigo': solicitud.id_solicitud}))					
		except Exception as e:
			raise e

	return render(request, 'editar_7.html', {'form': form, 'referencias': referencias, 'solicitud': solicitud} )



@transaction.atomic
def editar_8(request, codigo):
	solicitud = Solicitud.objects.get(pk=codigo)

	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
	else:
		form = SolicitudForm(request.POST, instance=solicitud)

		try:
			with transaction.atomic():
				solicitud = Solicitud.objects.get(id_solicitud=codigo)
				solicitud.proposito = None if request.POST.get('proposito') == '' else request.POST.get('proposito')
				solicitud.monto_inicial =  None if request.POST.get('monto_inicial') == '' else request.POST.get('monto_inicial')
				solicitud.origen_deposito =  None if request.POST.get('origen_deposito') == '' else request.POST.get('origen_deposito')
				solicitud.monto_mensual_estimado =  None if request.POST.get('monto_mensual_estimado') == '' else request.POST.get('monto_mensual_estimado')		
				solicitud.cod_vista = 9				
				solicitud.save()

				return redirect(reverse('editar_9', kwargs={'codigo': solicitud.id_solicitud}))

		except Exception as e:
			mensaje = 'error'

	return render(request, 'editar_8.html', {'form': form, 'solicitud': solicitud} )


@transaction.atomic
def editar_9(request, codigo):
	x = Beneficiario.objects.filter(id_solicitud=codigo)
	solicitud = Solicitud.objects.get(pk=codigo)

	if request.method == 'GET':
		form = SolicitudForm(instance=solicitud)
		beneficiarios = []
		for beneficiario in x:
			beneficiario = BeneficiarioForm(instance=beneficiario)
			beneficiarios.append(beneficiario)

	else:
		form = SolicitudForm(request.POST, instance=solicitud)	

	if request.POST:
		try:
			with transaction.atomic():
				nombre_completo = request.POST.getlist('nombre_completo[]')
				identidad = request.POST.getlist('identidad[]')
				parentesco = request.POST.getlist('parentesco[]')
				tipo_id = request.POST.getlist('tipo_id[]')
				porcentaje = request.POST.getlist('porcentaje[]')

				beneficiario = Beneficiario.objects.filter(id_solicitud=codigo).delete()

				counter = 0
				for x in nombre_completo:
					beneficiario = Beneficiario()
					solicitud = Solicitud.objects.get(id_solicitud=codigo)
					beneficiario.id_solicitud = solicitud
					beneficiario.nombre_completo = None if nombre_completo[counter] == '' else nombre_completo[counter]
					beneficiario.identidad = None if identidad[counter] == '' else identidad[counter]
					beneficiario.parentesco = None if parentesco[counter] == '' else parentesco[counter]
					beneficiario.tipo_id = None if tipo_id[counter] == '' else tipo_id[counter]
					beneficiario.porcentaje = None if porcentaje[counter] == '' else porcentaje[counter]
					solicitud.estado = 1
					solicitud.cod_vista = 10
					beneficiario.save()
					solicitud.save()
					counter += 1


				return redirect('menu_principal')
		except Exception as e:
			raise e

	return render(request, 'editar_9.html', {'form': form, 'beneficiarios': beneficiarios, 'solicitud': solicitud} )		





