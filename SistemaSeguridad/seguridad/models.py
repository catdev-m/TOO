# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AplicationParameter(models.Model):
    id_param = models.FloatField(primary_key=True)
    parameter = models.CharField(max_length=4000, blank=True, null=True)
    value = models.CharField(max_length=4000, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplication_parameter'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

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
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
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


class CompanyDepartmentLu(models.Model):
    id_depto = models.FloatField(primary_key=True)
    id_wunit = models.ForeignKey('CompanyWorkUnit', models.DO_NOTHING, db_column='id_wunit')
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_department_lu'


class CompanySectionLu(models.Model):
    id_section = models.FloatField(primary_key=True)
    id_depto = models.ForeignKey(CompanyDepartmentLu, models.DO_NOTHING, db_column='id_depto')
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_section_lu'


class CompanyWorkUnit(models.Model):
    id_wunit = models.FloatField(primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_work_unit'


class DatosTmp(models.Model):
    id = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=4000, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    date_nacimiento = models.DateField(blank=True, null=True)
    correo = models.CharField(max_length=300, blank=True, null=True)
    celular = models.TextField(blank=True, null=True)
    estatus = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_tmp'


class DepartmentLu(models.Model):
    id_department = models.FloatField(primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_lu'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GenderLu(models.Model):
    id_gender = models.FloatField(primary_key=True)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender_lu'


class HistoricalRoleUsr(models.Model):
    id_historical = models.FloatField(primary_key=True)
    id_role = models.FloatField()
    id_user = models.CharField(max_length=400)
    date_start = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historical_role_usr'


class HistoricalSalary(models.Model):
    id_salary = models.FloatField(primary_key=True)
    id_user = models.CharField(max_length=400, blank=True, null=True)
    main = models.CharField(max_length=1, blank=True, null=True)
    salary_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historical_salary'


class JobLu(models.Model):
    id_job = models.FloatField(primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_lu'


class LockedUser(models.Model):
    id_locked = models.FloatField(primary_key=True)
    id_user = models.CharField(max_length=400)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locked_user'


class MaritalStatusLu(models.Model):
    id_marital = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marital_status_lu'


class OptionMenu(models.Model):
    id_menu = models.FloatField(primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=4000, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option_menu'


class OptionRole(models.Model):
    id_role = models.OneToOneField('Role', models.DO_NOTHING, db_column='id_role', primary_key=True)
    id_menu = models.ForeignKey(OptionMenu, models.DO_NOTHING, db_column='id_menu')

    class Meta:
        managed = False
        db_table = 'option_role'
        unique_together = (('id_role', 'id_menu'),)


class OtpStaticStaticdevice(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    confirmed = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_static_staticdevice'


class OtpStaticStatictoken(models.Model):
    token = models.CharField(max_length=16, blank=True, null=True)
    device = models.ForeignKey(OtpStaticStaticdevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'otp_static_statictoken'


class OtpTotpTotpdevice(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    confirmed = models.BooleanField()
    key = models.CharField(max_length=80, blank=True, null=True)
    step = models.IntegerField()
    t0 = models.BigIntegerField()
    digits = models.IntegerField()
    tolerance = models.IntegerField()
    drift = models.IntegerField()
    last_t = models.BigIntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    throttling_failure_count = models.IntegerField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_totp_totpdevice'


class Person(models.Model):
    id_person = models.FloatField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    dui = models.CharField(max_length=10, blank=True, null=True)
    nit = models.CharField(max_length=16, blank=True, null=True)
    isss = models.CharField(max_length=10, blank=True, null=True)
    nup = models.CharField(max_length=12, blank=True, null=True)
    id_direccion = models.FloatField(blank=True, null=True)
    id_gender = models.FloatField(blank=True, null=True)
    id_marital_status = models.CharField(max_length=20, blank=True, null=True)
    id_job = models.FloatField(blank=True, null=True)
    id_depto = models.FloatField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class QuestionLu(models.Model):
    id_question = models.FloatField(primary_key=True)
    question = models.CharField(max_length=4000, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_lu'


class QuestionUsr(models.Model):
    id_ord_question = models.FloatField(primary_key=True)
    id_user = models.CharField(max_length=400)
    id_question = models.FloatField(blank=True, null=True)
    answer = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_usr'
        unique_together = (('id_ord_question', 'id_user'),)


class Role(models.Model):
    id_role = models.FloatField(primary_key=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class SeguridadDesbloqueo(models.Model):
    mascota = models.CharField(max_length=20, blank=True, null=True)
    colorfavorito = models.CharField(max_length=20, blank=True, null=True)
    nombrepadre = models.CharField(max_length=20, blank=True, null=True)
    numeroviajerofrecuente = models.CharField(max_length=20, blank=True, null=True)
    primernumerotelefonico = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguridad_desbloqueo'


class StateLu(models.Model):
    id_state = models.FloatField(primary_key=True)
    id_department = models.ForeignKey(DepartmentLu, models.DO_NOTHING, db_column='id_department')
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_lu'


class TwoFactorPhonedevice(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    confirmed = models.BooleanField()
    number = models.CharField(max_length=128, blank=True, null=True)
    key = models.CharField(max_length=40, blank=True, null=True)
    method = models.CharField(max_length=4, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'two_factor_phonedevice'


class Usr(models.Model):
    id_user = models.CharField(primary_key=True, max_length=400)
    password = models.CharField(max_length=250)
    id_person = models.ForeignKey(Person, models.DO_NOTHING, db_column='id_person')
    status = models.CharField(max_length=1, blank=True, null=True)
    locked = models.CharField(max_length=1, blank=True, null=True)
    first_login = models.CharField(max_length=1, blank=True, null=True)
    session_time = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usr'

class Prueba(models.Model):
    id = models.BigIntegerField( primary_key=True, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba'

class Desbloqueo(models.Model):
 id = models.AutoField( primary_key=True)
 mascota = models.CharField(max_length= 20,null = False)
 colorFavorito = models.CharField(max_length= 20,null= True)
 nombrePadre = models.CharField(max_length= 20,null= True)
 numeroViajeroFrecuente = models.CharField(max_length= 20,null= True)
 primerNumeroTelefonico = models.CharField(max_length= 20,null= True)
 #colorFavorito = models.CharField(max_length= 20)
 #nombrePadre = models.CharField(max_length= 20)
 #númeroViajeroFrecuente = models.CharField(max_length= 20)
 #primerNumeroTelefonico= models.CharField(max_length= 20)
 class Meta:
        ordering = ['mascota']
 
 def __str__(self):
     return self.mascota