# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from general.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group



PRODUCTO = (
	('','---------'),
	('A', 'Cuenta Ahorro'),
	('B', 'Cuenta Cheques'),
)

MONEDA = (
	('','---------'),
	('A', 'Lempiras '),
	('B', 'Dólares'),
)

SEXO = (
	('','---------'),
	('M', 'Masculino'),
	('F', 'Femenino'),
	
)

ESTADO_CIVIL = (
	('','---------'),
	('S', 'Soltero'),
	('C', 'Casado(a)'),
	('U', 'Union Libre'),
	('V', 'Viudo'),
	('D', 'Divorciado'),

)

TIPO_IDENTIFICACION = (
	('','---------'),
	('I', 'Identidad'),
	('P', 'Pasaporte'),
	('C', 'Carnét de residente'),
	('R', 'RTN'),
	('O', 'OTRO'),	
)

NIVEL_EDUCATIVO = (
	('','---------'),
	('N', 'Ninguno'),
	('P', 'Primaria'),
	('S', 'Secundaria'),
	('U', 'Universitaria'),
	('O', 'Otros'),
)

PROFESION = (
	('','---------'),
	('A', 'Asalariado'),
	('I', 'Independiente'),
	('J', 'Jubilado'),
	('E', 'Estudiante'),
	('M', 'Ama de casa'),
	('O', 'Otros'),
)



COMERC_INDIVIDUAL = (
	(True, 'Si'),
	(False, 'No'),
	)

CARGO_PUBLICO = (
	(True, 'Si'),
	(False, 'No'),
	)

FAMILIAR = (
	('','---------'),
	(True, 'Si'),
	(False, 'No'),
	)

TITULAR = (
	(True, 'Si'),
	(False, 'No'),
	)


FIRMA = (

	(True, 'Si'),
	(False, 'No'),
	)


NivelIngresosSMMV = (
	('','---------'),
	('A', 'De 0 a 3'),
	('B', 'De 4 a 6'),
	('C', 'De 7 a 10'),
	('D', 'De 11 a 20'),
	('E', 'De 21 a 50'),
	('F', 'De 50 en adelante'),

) 

Parentesco = (
	('','---------'),
	('C', 'Cónyugue'),
	('H', 'Hijo'),
	('I', 'Hija'),
	('P', 'Padre'),
	('M', 'Madre'),
	('F', 'Familiar'),
	('O', 'Otros'),
)




class SolicitudForm(ModelForm):
	producto = forms.ChoiceField(choices=PRODUCTO, label='Tipo de producto', required=False)
	moneda = forms.ChoiceField(choices=MONEDA, required=False)
	titular = forms.ChoiceField(widget=RadioSelect, choices=TITULAR, required=False)
	firma = forms.ChoiceField(widget=RadioSelect, choices=FIRMA, required=False)
	cargo_publico = forms.ChoiceField(widget=RadioSelect, choices=CARGO_PUBLICO, label='Ha desempeñado algún cargo público en los últimos 4 años?', required=False)
	estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL, required=False)
	sexo = forms.ChoiceField(choices=SEXO, required=False)
	comerciante_individual = forms.ChoiceField(widget=RadioSelect, choices=COMERC_INDIVIDUAL, required=False)
	tipo_identificacion = forms.ChoiceField(choices=TIPO_IDENTIFICACION, label='Tipo documento de identidad', required=False)
	nivel_ingresos_smmv = forms.ChoiceField(choices=NivelIngresosSMMV, label='Nivel aproximado de ingresos, según cantidad de SMMV', required=False)
	nivel_educativo = forms.ChoiceField(choices=NIVEL_EDUCATIVO, required=False)
	profesion = forms.ChoiceField(choices=PROFESION, label='Profesión', required=False)
	comerciante_individual = forms.ChoiceField(widget=RadioSelect, choices=COMERC_INDIVIDUAL, required=False)
	nivel_ingresos_smmv = forms.ChoiceField(choices=NivelIngresosSMMV, label='Nivel aproximado de ingresos, según cantidad de SMMV ', required=False)
	cargo_publico = forms.ChoiceField(widget=RadioSelect, choices=CARGO_PUBLICO, required=False)



	class Meta:
		model = Solicitud
		fields = "__all__"
		exclude = []
		labels = {'lugar_nacimiento': ('Lugar de nacimiento'),
		'cod_pais_nacimiento': ('País de nacimiento'),
		'cod_depto_nacimiento': ('Departamento de nacimiento'),
		'cod_municipio': ('Municipio de nacimiento'),
		'cod_depto_direccion': ('Departamento Dirección'),
		'cod_mun_direccion': ('Municipio Dirección'),
		'cod_col_direccion': ('Barrio o Colonia'),
		'telefono_casa': ('Teléfono Casa'),
		'rtn': ('RTN'),
		'direccion_detallada': ('Dirección detallada'),
		'telefono2': ('Teléfono 2'),
		'correo_electronico': ('Correo electrónico'),
		
		'cod_pais_residencia': ('En caso de ser extranjero, país de residencia'),
		'cod_actividad_economica': ('Actividad económica'),
		'nombre_empresa': ('Nombre empresa en la que labora'),
		'cod_depto_direccion_empresa': ('Departamento'),
		'cod_mun_direccion_empresa': ('Municipio'),
		'direccion_detallada_empresa': ('Dirección detallada empresa'),
		'telefono_empresa': ('Teléfono empresa'),
		'posicion_empresa': ('Posición/Cargo que desempeña'),
		'antiguedad_meses': ('Tiempo de laborar'),
		'detalle_o_giro': ('Detalle el nombre y giro del negocio'),
		'nivel_ingresos_smmv': ('Nivel aproximado de ingresos, según cantidad de SMMV'),
		'cod_institucion_pub': ('Nombre de la institución'),
		'cant_personas': ('Cantidad de personas que dependen de usted económicamente'),
		'proposito': ('Propósito de la cuenta'),
		'monto_inicial': ('Monto del depósito inicial'),
		'origen_deposito': ('Orígen del depósito inicial'),
		'monto_mensual_estimado': ('Monto mensual estimado que ingresará a la cuenta'),
		


		}	


class DependienteForm(ModelForm):

	tipo_id = forms.ChoiceField(choices=TIPO_IDENTIFICACION, label='Tipo de identificación', required=False)
	parentesco = forms.ChoiceField(choices=Parentesco, required=False)


	class Meta:
		model = Dependiente
		fields = "__all__"
		exclude = []
		labels = {}


class ReferenciaForm(ModelForm):

	familiar = forms.ChoiceField(choices=FAMILIAR, required=False)

	class Meta:
		model = Referencia
		fields = "__all__"
		exclude = []
		labels = { 'telefono': ('Teléfono'), }


class BeneficiarioForm(ModelForm):	
	tipo_id = forms.ChoiceField(choices=TIPO_IDENTIFICACION, label='Tipo de identificación', required=False)
	parentesco = forms.ChoiceField(choices=Parentesco, required=False)

	class Meta:
		model = Beneficiario
		fields = "__all__"
		exclude = []
		labels = {}		















