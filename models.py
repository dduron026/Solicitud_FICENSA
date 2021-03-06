# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Actividadeseconomicas(models.Model):
    codactividadeconomica = models.ForeignKey('Solicitudes', models.DO_NOTHING, db_column='CodActividadEconomica', primary_key=True)  # Field name made lowercase.
    descactividad = models.CharField(db_column='DescActividad', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActividadesEconomicas'


class Beneficiarios(models.Model):
    codbeneficiario = models.IntegerField(db_column='CodBeneficiario', primary_key=True)  # Field name made lowercase.
    idsolicitud = models.ForeignKey('Solicitudes', models.DO_NOTHING, db_column='IdSolicitud', blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    parentesco = models.CharField(db_column='Parentesco', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipoid = models.CharField(db_column='TipoId', max_length=1, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.IntegerField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Beneficiarios'


class Colonias(models.Model):
    codcolonia = models.IntegerField(db_column='CodColonia', primary_key=True)  # Field name made lowercase.
    codmunicipio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='CodMunicipio', blank=True, null=True)  # Field name made lowercase.
    descripcioncolinia = models.CharField(db_column='DescripcionColinia', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Colonias'


class Departamentos(models.Model):
    coddepartamento = models.IntegerField(db_column='CodDepartamento', primary_key=True)  # Field name made lowercase.
    codpais = models.ForeignKey('Paises', models.DO_NOTHING, db_column='CodPais', blank=True, null=True)  # Field name made lowercase.
    descripciondepto = models.CharField(db_column='DescripcionDepto', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Dependientes(models.Model):
    coddependiente = models.IntegerField(db_column='CodDependiente', primary_key=True)  # Field name made lowercase.
    idsolicitud = models.ForeignKey('Solicitudes', models.DO_NOTHING, db_column='IdSolicitud', blank=True, null=True)  # Field name made lowercase.
    parentesco = models.CharField(db_column='Parentesco', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipoid = models.CharField(db_column='TipoId', max_length=1, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dependientes'


class Instituciones(models.Model):
    codinstituciones = models.IntegerField(db_column='CodInstituciones', primary_key=True)  # Field name made lowercase.
    descripcioninst = models.CharField(db_column='DescripcionInst', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instituciones'


class Municipios(models.Model):
    codmunicipio = models.IntegerField(db_column='CodMunicipio', primary_key=True)  # Field name made lowercase.
    coddepartamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDepartamento', blank=True, null=True)  # Field name made lowercase.
    descripcionmunicipio = models.CharField(db_column='DescripcionMunicipio', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Municipios'


class Paises(models.Model):
    codpais = models.IntegerField(db_column='CodPais', primary_key=True)  # Field name made lowercase.
    descripcionpais = models.CharField(db_column='DescripcionPais', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Paises'


class Referencias(models.Model):
    codreferencia = models.IntegerField(db_column='CodReferencia', primary_key=True)  # Field name made lowercase.
    idsolicitud = models.ForeignKey('Solicitudes', models.DO_NOTHING, db_column='IdSolicitud', blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    telelfono = models.CharField(db_column='Telelfono', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familiar = models.NullBooleanField(db_column='Familiar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referencias'


class Solicitudes(models.Model):
    idsolicitud = models.IntegerField(db_column='IdSolicitud', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=1, blank=True, null=True)  # Field name made lowercase.
    moneda = models.CharField(db_column='Moneda', max_length=1, blank=True, null=True)  # Field name made lowercase.
    titular = models.NullBooleanField(db_column='Titular')  # Field name made lowercase.
    firma = models.NullBooleanField(db_column='Firma')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    identidad = models.CharField(db_column='Identidad', max_length=13, blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.CharField(db_column='FechaNacimiento', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codpaisnacimiento = models.ForeignKey(Paises, models.DO_NOTHING, db_column='CodPaisNacimiento', blank=True, null=True)  # Field name made lowercase.
    coddeptonacimiento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDeptoNacimiento', blank=True, null=True)  # Field name made lowercase.
    codmunicipio = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='CodMunicipio', blank=True, null=True)  # Field name made lowercase.
    lugarnacimiento = models.CharField(db_column='LugarNacimiento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.IntegerField(db_column='Nacionalidad', blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nombreconyuge = models.CharField(db_column='NombreConyuge', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipoidentificacion = models.CharField(db_column='TipoIdentificacion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rtn = models.CharField(db_column='RTN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    coddeptodireccion = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDeptoDireccion', blank=True, null=True)  # Field name made lowercase.
    codmundireccion = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='CodMunDireccion', blank=True, null=True)  # Field name made lowercase.
    codcoldireccion = models.ForeignKey(Colonias, models.DO_NOTHING, db_column='CodColDireccion', blank=True, null=True)  # Field name made lowercase.
    direcciondetallada = models.CharField(db_column='DireccionDetallada', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=200, blank=True, null=True)  # Field name made lowercase.
    casa = models.CharField(db_column='Casa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    telefonocasa = models.CharField(db_column='TelefonoCasa', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='Telefono2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codpaisresidencia = models.ForeignKey(Paises, models.DO_NOTHING, db_column='CodPaisResidencia', blank=True, null=True)  # Field name made lowercase.
    niveleducativo = models.CharField(db_column='NivelEducativo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    correoelectronico = models.CharField(db_column='CorreoElectronico', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profesion = models.CharField(db_column='Profesion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    codactividadeconomica = models.IntegerField(db_column='CodActividadEconomica', blank=True, null=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='NombreEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coddeptodireccionempresa = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='CodDeptoDireccionEmpresa', blank=True, null=True)  # Field name made lowercase.
    codmundireccionempresa = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='CodMunDireccionEmpresa', blank=True, null=True)  # Field name made lowercase.
    direcciondetalladaempresa = models.CharField(db_column='DireccionDetalladaEmpresa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    posicionempresa = models.CharField(db_column='PosicionEmpresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    antiguedadmeses = models.IntegerField(db_column='AntiguedadMeses', blank=True, null=True)  # Field name made lowercase.
    comercianteindividual = models.NullBooleanField(db_column='ComercianteIndividual')  # Field name made lowercase.
    detalleogiro = models.CharField(db_column='DetalleoGiro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nivelingresossmmv = models.CharField(db_column='NivelIngresosSMMV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cargopublico = models.NullBooleanField(db_column='CargoPublico')  # Field name made lowercase.
    codinstitucionpub = models.ForeignKey(Instituciones, models.DO_NOTHING, db_column='CodInstitucionPub', blank=True, null=True)  # Field name made lowercase.
    cantpersonas = models.IntegerField(db_column='CantPersonas', blank=True, null=True)  # Field name made lowercase.
    proposito = models.CharField(db_column='Proposito', max_length=1, blank=True, null=True)  # Field name made lowercase.
    montoinicial = models.IntegerField(db_column='MontoInicial', blank=True, null=True)  # Field name made lowercase.
    origendeposito = models.CharField(db_column='OrigenDeposito', max_length=1, blank=True, null=True)  # Field name made lowercase.
    montomensualestimado = models.IntegerField(db_column='MontoMensualEstimado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Solicitudes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
