from django.db import models
class Uf(models.Model):
    id_uf = models.IntegerField(primary_key=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'UF'

class Bairros(models.Model):
    id_bairro = models.IntegerField(primary_key=True)
    id_cidade = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'bairros'


class Cidades(models.Model):
    id_cidade = models.IntegerField(primary_key=True)
    id_uf = models.ForeignKey(Uf, models.DO_NOTHING, db_column='id_uf', blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'cidades'

class Endereco(models.Model):
    idendereco = models.IntegerField(db_column='idEndereco', primary_key=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'endereco'


class Filial(models.Model):
    idfilial = models.AutoField(db_column='idFilial', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idendereco = models.IntegerField(db_column='idEndereco', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'filial'


class Perfil(models.Model):
    idperfil = models.AutoField(db_column='IdPerfil', primary_key=True)  # Field name made lowercase.
    atribuicao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'perfil'


class Pessoa(models.Model):
    idpessoa = models.IntegerField(db_column='idPessoa', primary_key=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cnh = models.CharField(db_column='CNH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    rntrc = models.IntegerField(db_column='RNTRC', blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='e-mail', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    idusuario = models.IntegerField(db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    idfilial = models.IntegerField(db_column='idFilial', blank=True, null=True)  # Field name made lowercase.
    idendereco = models.IntegerField(db_column='idEndereco', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pessoa'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=45, blank=True, null=True)
    senha = models.CharField(max_length=45, blank=True, null=True)
    idperfil = models.CharField(db_column='idPerfil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'usuario'
