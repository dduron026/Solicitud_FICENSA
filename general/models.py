from __future__ import unicode_literals

from django.db import models


class Actividadeseconomicas(models.Model):
	cod_actividad_economica = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='CodActividadEconomica', primary_key=True)  # Field name made lowercase.
	desc_actividad = models.CharField(db_column='DescActividad', max_length=1000, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[ActividadesEconomicas'
	


class Beneficiario(models.Model):
	cod_beneficiario = models.AutoField(db_column='CodBeneficiario', primary_key=True)  # Field name made lowercase.
	id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='IdSolicitud', blank=True, null=True)  # Field name made lowercase.
	nombre_completo = models.CharField(db_column='NombreCompleto', max_length=200, blank=True, null=True)  # Field name made lowercase.
	identidad = models.CharField(db_column='ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
	parentesco = models.CharField(db_column='Parentesco', max_length=1, blank=True, null=True)  # Field name made lowercase.
	tipo_id = models.CharField(db_column='TipoId', max_length=1, blank=True, null=True)  # Field name made lowercase.
	porcentaje = models.IntegerField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Beneficiarios'


class Colonia(models.Model):
	cod_colonia = models.AutoField(db_column='CodColonia', primary_key=True)  # Field name made lowercase.
	cod_municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='CodMunicipio', blank=True, null=True)  # Field name made lowercase.
	descripcion_colonia = models.CharField(db_column='DescripcionColonia', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Colonias'

	def __unicode__(self):
		return self.descripcion_colonia		




class Departamento(models.Model):
	cod_departamento = models.AutoField(db_column='CodDepartamento', primary_key=True)  # Field name made lowercase.
	cod_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='CodPais', blank=True, null=True)  # Field name made lowercase.
	descripcion_depto = models.CharField(db_column='DescripcionDepto', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Departamentos'

	def __unicode__(self):
		return self.descripcion_depto		


class Dependiente(models.Model):
	cod_dependiente = models.AutoField(db_column='CodDependiente', primary_key=True)  # Field name made lowercase.
	id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='IdSolicitud', blank=True, null=True)  # Field name made lowercase.
	parentesco = models.CharField(db_column='Parentesco', max_length=1, blank=True, null=True)  # Field name made lowercase.
	tipo_id = models.CharField(db_column='TipoId', max_length=1, blank=True, null=True)  # Field name made lowercase.
	identidad = models.CharField(db_column='ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
	nombre_completo = models.CharField(db_column='NombreCompleto', max_length=200, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Dependientes'


class Institucion(models.Model):
	cod_instituciones = models.AutoField(db_column='CodInstituciones', primary_key=True)  # Field name made lowercase.
	descripcion_inst = models.CharField(db_column='DescripcionInst', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Instituciones'

	def __unicode__(self):
		return self.descripcion_inst	


class Municipio(models.Model):
	cod_municipio = models.AutoField(db_column='CodMunicipio', primary_key=True)  # Field name made lowercase.
	cod_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='CodDepartamento', blank=True, null=True)  # Field name made lowercase.
	descripcion_municipio = models.CharField(db_column='DescripcionMunicipio', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Municipios'

	def __unicode__(self):
		return self.descripcion_municipio		


class Pais(models.Model):
	cod_pais = models.AutoField(db_column='CodPais', primary_key=True)  # Field name made lowercase.
	descripcion_pais = models.CharField(db_column='DescripcionPais', max_length=100, blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Paises'

	def __unicode__(self):
		return self.descripcion_pais


class Referencia(models.Model):
	cod_referencia = models.AutoField(db_column='CodReferencia', primary_key=True)  # Field name made lowercase.
	id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='IdSolicitud', related_name='IdSolicitud', blank=True, null=True)  # Field name made lowercase.
	nombre_completo = models.CharField(db_column='NombreCompleto', max_length=200, blank=True, null=True)  # Field name made lowercase.
	telefono = models.CharField(db_column='Telefono', max_length=50, blank=True, null=True)  # Field name made lowercase.
	familiar = models.NullBooleanField(db_column='Familiar')  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Referencias'


class Solicitud(models.Model):
	id_solicitud = models.AutoField(db_column='IdSolicitud', primary_key=True)  # Field name made lowercase.
	cod_vista = models.IntegerField(db_column='CodVista', blank=True, null=True)
	producto = models.CharField(db_column='Producto', max_length=1, blank=True, null=True)  # Field name made lowercase.
	moneda = models.CharField(db_column='Moneda', max_length=1, blank=True, null=True)  # Field name made lowercase.
	titular = models.NullBooleanField(db_column='Titular')  # Field name made lowercase.
	firma = models.NullBooleanField(db_column='Firma')  # Field name made lowercase.
	estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
	identidad = models.CharField(db_column='Identidad', max_length=13, blank=True, null=True)  # Field name made lowercase.
	nombre_completo = models.CharField(db_column='NombreCompleto', max_length=100, blank=True, null=True)
	fecha_nacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
	cod_pais_nacimiento = models.ForeignKey(Pais, models.DO_NOTHING, db_column='CodPaisNacimiento', blank=True, null=True)  # Field name made lowercase.
	cod_depto_nacimiento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='CodDeptoNacimiento', related_name='CodDeptoNacimiento_depto', blank=True, null=True)  # Field name made lowercase.
	cod_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='CodMunicipio', related_name='CodMunicipio_muni', blank=True, null=True)  # Field name made lowercase.
	lugar_nacimiento = models.CharField(db_column='LugarNacimiento', max_length=50, blank=True, null=True)  # Field name made lowercase.
	nacionalidad = models.IntegerField(db_column='Nacionalidad', blank=True, null=True)  # Field name made lowercase.
   
	# vista2
	estado_civil = models.CharField(db_column='EstadoCivil', max_length=1, blank=True, null=True)  # Field name made lowercase.
	sexo = models.CharField(db_column='Sexo', max_length=1, blank=True, null=True)  # Field name made lowercase.
	nombre_conyuge = models.CharField(db_column='NombreConyuge', max_length=100, blank=True, null=True)  # Field name made lowercase.
	tipo_identificacion = models.CharField(db_column='TipoIdentificacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
	rtn = models.CharField(db_column='RTN', max_length=14, blank=True, null=True)  # Field name made lowercase.
	direccion_detallada = models.CharField(db_column='DireccionDetallada', max_length=200, blank=True, null=True)  # Field name made lowercase.  
	cod_depto_direccion = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='CodDeptoDireccion', related_name='CodDeptoDireccion_depto', blank=True, null=True)  # Field name made lowercase.
	cod_mun_direccion = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='CodMunDireccion', blank=True, null=True)  # Field name made lowercase.
	cod_col_direccion = models.ForeignKey(Colonia, models.DO_NOTHING, db_column='CodColDireccion', blank=True, null=True)  # Field name made lowercase.
	referencia = models.CharField(db_column='Referencia', max_length=200, blank=True, null=True)  # Field name made lowercase.
	casa = models.CharField(db_column='Casa', max_length=200, blank=True, null=True)  # Field name made lowercase.
	telefono_casa = models.CharField(db_column='TelefonoCasa', max_length=20, blank=True, null=True)  # Field name made lowercase.
	
	# vista 3
	telefono2 = models.CharField(db_column='Telefono2', max_length=20, blank=True, null=True)  # Field name made lowercase.
	celular = models.CharField(db_column='Celular', max_length=20, blank=True, null=True)  # Field name made lowercase.
	fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
	cod_pais_residencia = models.ForeignKey(Pais, models.DO_NOTHING, db_column='CodPaisResidencia', related_name='CodPaisResidencia_pais', blank=True, null=True)  # Field name made lowercase.
	nivel_educativo = models.CharField(db_column='NivelEducativo', max_length=1, blank=True, null=True)  # Field name made lowercase.
	correo_electronico = models.CharField(db_column='CorreoElectronico', max_length=50, blank=True, null=True)  # Field name made lowercase.
	profesion = models.CharField(db_column='Profesion', max_length=1, blank=True, null=True)  # Field name made lowercase.
	cod_actividad_economica = models.IntegerField(db_column='CodActividadEconomica', blank=True, null=True)  # Field name made lowercase.
	cod_depto_direccion_empresa = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='CodDeptoDireccionEmpresa', blank=True, null=True)  # Field name made lowercase.
	nombre_empresa = models.CharField(db_column='NombreEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.

	# vista4
	cod_mun_direccion_empresa = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='CodMunDireccionEmpresa', related_name='CodMunDireccionEmpresa_muni', blank=True, null=True)  # Field name made lowercase.
	telefono_empresa = models.CharField(db_column='TelefonoEmpresa', max_length=20, blank=True, null=True)
	direccion_detallada_empresa = models.CharField(db_column='DireccionDetalladaEmpresa', max_length=200, blank=True, null=True)  # Field name made lowercase.
	posicion_empresa = models.CharField(db_column='PosicionEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
	antiguedad_meses = models.IntegerField(db_column='AntiguedadMeses', blank=True, null=True)  # Field name made lowercase.
	comerciante_individual = models.NullBooleanField(db_column='ComercianteIndividual')  # Field name made lowercase.
	detalle_o_giro = models.CharField(db_column='DetalleoGiro', max_length=100, blank=True, null=True)  # Field name made lowercase.
	nivel_ingresos_smmv = models.CharField(db_column='NivelIngresosSMMV', max_length=1, blank=True, null=True)  # Field name made lowercase.
	
	# vista 5
	cargo_publico = models.NullBooleanField(db_column='CargoPublico')  # Field name made lowercase.
	cod_institucion_pub = models.ForeignKey(Institucion, models.DO_NOTHING, db_column='CodInstitucionPub', blank=True, null=True)  # Field name made lowercase.
	cant_personas = models.IntegerField(db_column='CantPersonas', blank=True, null=True)  # Field name made lowercase.
	
    # vista 8
	proposito = models.CharField(db_column='Proposito', max_length=1, blank=True, null=True)  # Field name made lowercase.
	monto_inicial = models.IntegerField(db_column='MontoInicial', blank=True, null=True)  # Field name made lowercase.
	origen_deposito = models.CharField(db_column='OrigenDeposito', max_length=1, blank=True, null=True)  # Field name made lowercase.
	monto_mensual_estimado = models.IntegerField(db_column='MontoMensualEstimado', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'Sol].[Solicitudes'














