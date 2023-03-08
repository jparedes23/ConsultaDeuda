from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import usuarioManager

# Create your models here.



class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    tipoUsuario = models.CharField(max_length=40, choices=[
       ('ADMINISTRADOR', 'ADMINISTRADOR'),
       ('CLIENTE','CLIENTE')
    ])

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    USERNAME_FIELD ='correo'
    REQUIRED_FIELDS =['nombre', 'apellido', 'tipoUsuario']


    objects = usuarioManager()
    class Meta:
        db_table= 'usuarios'


class Deuda(models.Model):
    key_deuda = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    tipo_deuda = models.CharField(max_length=3)
    key_cont = models.ForeignKey('Contribuyente', models.DO_NOTHING, db_column='key_cont')
    cargo = models.DecimalField(max_digits=10, decimal_places=2)
    estado_deuda = models.ForeignKey('EstDeuda', models.DO_NOTHING, db_column='estado_deuda')
    fecha_nace = models.DateTimeField(blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    condicion = models.CharField(max_length=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    key_tributo = models.SmallIntegerField(blank=True, null=True)
    imp_baja = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    observa = models.CharField(max_length=300, blank=True, null=True)
    inte1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inte2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cargo_rec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    key_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='key_periodo', blank=True, null=True)
    via = models.CharField(max_length=3, blank=True, null=True)
    w_usuario = models.CharField(max_length=20, blank=True, null=True)
    f_reg = models.DateTimeField(blank=True, null=True)
    f_time = models.DateTimeField(blank=True, null=True)
    sw_int = models.CharField(max_length=1, blank=True, null=True)
    import_int = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cuota = models.SmallIntegerField(blank=True, null=True)
    tipo_moneda = models.CharField(max_length=1, blank=True, null=True)
    estado_coa = models.CharField(max_length=2, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    num_periodo2 = models.SmallIntegerField(blank=True, null=True)
    mes = models.CharField(max_length=30, blank=True, null=True)
    key_recibo_agua = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    key_predio = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deuda'


class EstDeuda(models.Model):
    key_estdeuda = models.CharField(primary_key=True, max_length=2)
    estdeuda = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'est_deuda'

class Periodo(models.Model):
    key_periodo = models.IntegerField(primary_key=True)
    key_tributo = models.SmallIntegerField()
    anio = models.IntegerField()
    num_periodo = models.SmallIntegerField()
    f_inicio = models.DateTimeField(blank=True, null=True)
    f_vencim = models.DateTimeField(blank=True, null=True)
    tipo_periodo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'

class Auxiliar(models.Model):
    key_auxiliar = models.OneToOneField('Contribuyente', models.DO_NOTHING, db_column='key_auxiliar', primary_key=True)
    iniciales = models.CharField(max_length=8)
    est_auxiliar = models.CharField(max_length=1)
    f_asigna = models.DateTimeField(blank=True, null=True)
    nombres = models.CharField(db_column='Nombres', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auxiliar'


class Recibo(models.Model):
    num_recibo = models.DecimalField(max_digits=8, decimal_places=0)
    key_recibo = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    key_auxiliar = models.ForeignKey('Auxiliar', models.DO_NOTHING, db_column='key_auxiliar', blank=True, null=True)
    num_emision = models.SmallIntegerField()
    f_emision = models.DateTimeField()
    estado_recibo = models.CharField(max_length=1)
    tipo_recibo = models.CharField(max_length=1)
    lote = models.IntegerField(blank=True, null=True)
    serie = models.CharField(max_length=10, blank=True, null=True)
    w_usuario = models.CharField(max_length=50, blank=True, null=True)
    w_fecha = models.DateTimeField(blank=True, null=True)
    w_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibo'


class ReciboAgua(models.Model):
    key_recibo_agua = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    num_recibo_agua = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    key_cont = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    datos_generales = models.CharField(max_length=150, blank=True, null=True)
    key_predio = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    saldo_agua = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saldo_alcantarillado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saldo_salubridad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ga = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    interes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    key_periodo = models.IntegerField(blank=True, null=True)
    num_periodo = models.SmallIntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=150, blank=True, null=True)
    fecha_reg = models.DateTimeField(blank=True, null=True)
    usuario_reg = models.CharField(max_length=50, blank=True, null=True)
    anio_periodo = models.SmallIntegerField(blank=True, null=True)
    danterior = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    
    
    class Meta:
        managed = False
        db_table = 'recibo_agua'

class Direccion(models.Model):
    key_dir = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    agregado = models.CharField(max_length=30, blank=True, null=True)
    key_barrio = models.ForeignKey('Barrio', models.DO_NOTHING, db_column='key_barrio')
    tipo_dir = models.CharField(max_length=1, blank=True, null=True)
    key_calle = models.ForeignKey('Calles', models.DO_NOTHING, db_column='key_calle', blank=True, null=True)
    num_calle = models.CharField(max_length=30, blank=True, null=True)
    sw_dirfiscal = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Contribuyente(models.Model):
    key_cont = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    key_dir = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='key_dir', blank=True, null=True)
    tipo_pers = models.CharField(max_length=1)
    nro_doc = models.CharField(max_length=20, blank=True, null=True)
    key_condcontrib = models.ForeignKey('CondContribuyente', models.DO_NOTHING, db_column='key_condcontrib', blank=True, null=True)
    tipo_cont = models.CharField(max_length=1, blank=True, null=True)
    referencia = models.CharField(max_length=30, blank=True, null=True)
    w_usuario = models.CharField(max_length=20, blank=True, null=True)
    key_tipodoc = models.SmallIntegerField(blank=True, null=True)
    ap_paterno = models.CharField(max_length=30, blank=True, null=True)
    ap_materno = models.CharField(max_length=30, blank=True, null=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    validacion = models.SmallIntegerField(blank=True, null=True)
    freg = models.DateTimeField(blank=True, null=True)
    comunicado = models.CharField(max_length=2, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    f_comunicado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Contribuyente'




class CondContribuyente(models.Model):
    key_condcontrib = models.SmallIntegerField(primary_key=True)
    desc_condcontrib = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cond_Contribuyente'

class Departamento(models.Model):
    key_departamento = models.SmallIntegerField(primary_key=True)
    departamento = models.CharField(db_column='Departamento', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Provincia(models.Model):
    key_provincia = models.SmallIntegerField(db_column='key_Provincia', primary_key=True)  # Field name made lowercase.
    key_departamento = models.SmallIntegerField(db_column='Key_Departamento')  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Provincia'



class Distrito(models.Model):
    key_distrito = models.IntegerField(db_column='Key_Distrito', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    key_provincia = models.SmallIntegerField(db_column='key_Provincia', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distrito'


class Barrio(models.Model):
    key_barrio = models.IntegerField(primary_key=True)
    key_tlugar = models.SmallIntegerField(blank=True, null=True)
    key_sector = models.IntegerField(blank=True, null=True)
    nom_barrio = models.CharField(max_length=80)
    cod_barrio = models.CharField(max_length=7, blank=True, null=True)
    t_aran = models.CharField(max_length=1, blank=True, null=True)
    crit_orden = models.SmallIntegerField(blank=True, null=True)
    key_distrito = models.ForeignKey('Distrito', models.DO_NOTHING, db_column='key_distrito', blank=True, null=True)
    key_zona_rs = models.SmallIntegerField(blank=True, null=True)
    key_zona_bc = models.SmallIntegerField(blank=True, null=True)
    key_zona_sc = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barrio'

class Calles(models.Model):
    key_calle = models.IntegerField(primary_key=True)
    key_tcalle = models.SmallIntegerField()
    nom_calle = models.CharField(max_length=100)
    t_aran = models.CharField(max_length=1, blank=True, null=True)
    descrip = models.CharField(max_length=30, blank=True, null=True)
    codcalle_ant = models.CharField(max_length=5, blank=True, null=True)
    correlativo = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calles'


class Predio(models.Model):
    key_predio = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    tipo_predio = models.CharField(max_length=1)
    cod_catrastal = models.CharField(max_length=15, blank=True, null=True)
    nom_predio = models.CharField(max_length=100, blank=True, null=True)
    f_modificacion = models.DateTimeField(blank=True, null=True)
    num_condom = models.SmallIntegerField(blank=True, null=True)
    actualizado = models.CharField(max_length=1, blank=True, null=True)
    cod_registral = models.CharField(max_length=20, blank=True, null=True)
    xp = models.SmallIntegerField(blank=True, null=True)
    xa = models.SmallIntegerField(blank=True, null=True)
    metros_lineales = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    areas_verdes = models.SmallIntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=150, blank=True, null=True)
    num_licencia = models.CharField(max_length=10, blank=True, null=True)
    fisc = models.CharField(max_length=1, blank=True, null=True)
    w_usuario = models.CharField(max_length=30, blank=True, null=True)
    fecha_reg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predio'

class PredioAgua(models.Model):
    key_predio = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    ano_fiscal = models.SmallIntegerField(blank=True, null=True)
    key_upredio = models.SmallIntegerField(blank=True, null=True)
    situacion = models.CharField(max_length=1, blank=True, null=True)
    agua = models.CharField(max_length=1, blank=True, null=True)
    alcantarillado = models.CharField(max_length=1, blank=True, null=True)
    salubridad = models.CharField(max_length=1, blank=True, null=True)
    key_periodo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predio_agua'

class ContribuyentePredio(models.Model):
    key_predio = models.OneToOneField(Predio, models.DO_NOTHING, db_column='key_predio', primary_key=True)
    key_cont = models.DecimalField(max_digits=8, decimal_places=0)
    f_traspaso = models.DateField()
    cond_contrib = models.CharField(max_length=1)
    porc_condom = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    num_anexo = models.SmallIntegerField(blank=True, null=True)
    est_predio = models.CharField(max_length=1, blank=True, null=True)
    porc_afecto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    est_contrib = models.CharField(max_length=1, blank=True, null=True)
    key_regimen = models.ForeignKey('Regimen', models.DO_NOTHING, db_column='key_regimen', blank=True, null=True)
    num_exon = models.ForeignKey('PredioExon', models.DO_NOTHING, db_column='num_exon', blank=True, null=True)
    resolucion = models.CharField(max_length=30, blank=True, null=True)
    expediente = models.CharField(max_length=30, blank=True, null=True)
    anio_ini = models.IntegerField(blank=True, null=True)
    trim_ini = models.SmallIntegerField(blank=True, null=True)
    anio_fin = models.IntegerField(blank=True, null=True)
    trim_fin = models.SmallIntegerField(blank=True, null=True)
    w_usuario = models.CharField(max_length=30, blank=True, null=True)
    f_hora = models.TextField(blank=True, null=True)  # This field type is a guess.
    porc_afecto_arb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha_adq = models.DateTimeField(blank=True, null=True)
    tipo_cont = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Contribuyente_predio'
        unique_together = (('key_predio', 'key_cont', 'f_traspaso'),)

class Regimen(models.Model):
    key_regimen = models.SmallIntegerField(primary_key=True)
    desc_regimen = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'regimen'

class PredioExon(models.Model):
    key_resolucion = models.ForeignKey('Resolucion', models.DO_NOTHING, db_column='key_resolucion')
    num_exon = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    f_emitida = models.DateTimeField(blank=True, null=True)
    periodo_ini = models.IntegerField(blank=True, null=True)
    trimestre_ini = models.IntegerField(blank=True, null=True)
    periodo_venc = models.IntegerField(blank=True, null=True)
    trimestre_venc = models.CharField(max_length=4, blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'predio_exon'

class Fraccionamiento(models.Model):
    key_frac = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    key_cont = models.DecimalField(max_digits=8, decimal_places=0)
    tipo_frac = models.CharField(max_length=3)
    f_fraccion = models.DateTimeField(blank=True, null=True)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    n_cuotas = models.SmallIntegerField(blank=True, null=True)
    f_inicio = models.DateTimeField(blank=True, null=True)
    n_dias = models.IntegerField(blank=True, null=True)
    numerofrac = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    observacion = models.CharField(max_length=350, blank=True, null=True)
    factor = models.FloatField(blank=True, null=True)
    wusuario = models.CharField(max_length=20, blank=True, null=True)
    freg = models.DateTimeField(blank=True, null=True)
    fhora = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    via = models.CharField(max_length=3, blank=True, null=True)
    resol_emi = models.CharField(max_length=1, blank=True, null=True)
    costas = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    gastos = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nroresjef = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    grantia = models.CharField(max_length=10, blank=True, null=True)
    decreto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    decretperiodo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fraccionamiento'




class Resolucion(models.Model):
    key_resolucion = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    num_resol = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    f_resolucion = models.DateTimeField(blank=True, null=True)
    key_cont = models.DecimalField(max_digits=8, decimal_places=0)
    key_reclamo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    key_inftecnico = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tipo_res = models.CharField(max_length=1, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    f_notificado = models.DateTimeField(blank=True, null=True)
    desc_notificado = models.CharField(max_length=30, blank=True, null=True)
    w_usuario = models.CharField(max_length=30, blank=True, null=True)
    w_date = models.DateTimeField(blank=True, null=True)
    f_time = models.DateTimeField(blank=True, null=True)
    w_time = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    key_situacion = models.CharField(max_length=3, blank=True, null=True)
    unidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='unidad', blank=True, null=True)
    via = models.CharField(max_length=3, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    key_docum = models.SmallIntegerField(blank=True, null=True)
    nro_doc = models.CharField(max_length=15, blank=True, null=True)
    f_coactivo = models.DateTimeField(blank=True, null=True)
    notificado = models.CharField(max_length=2, blank=True, null=True)
    condicion = models.CharField(max_length=2, blank=True, null=True)
    f_recepcion = models.DateTimeField(blank=True, null=True)
    key_frac = models.ForeignKey('Fraccionamiento', models.DO_NOTHING, db_column='key_frac', blank=True, null=True)
    sistema = models.CharField(max_length=3, blank=True, null=True)
    f_rentas = models.DateTimeField(blank=True, null=True)
    condicion1 = models.CharField(max_length=2, blank=True, null=True)
    f_recepcion1 = models.DateTimeField(blank=True, null=True)
    idlote = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    swp = models.CharField(max_length=1, blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    det_anulacion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resolucion'


class Unidad(models.Model):
    key_unidad = models.IntegerField(primary_key=True)
    desc_unidad = models.CharField(max_length=95, blank=True, null=True)
    siglas = models.CharField(max_length=10, blank=True, null=True)
    tuot_ini = models.CharField(max_length=5, blank=True, null=True)
    tuot_fin = models.CharField(max_length=5, blank=True, null=True)
    key_area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad'



