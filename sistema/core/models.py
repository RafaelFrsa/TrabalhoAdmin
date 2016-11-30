from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Cliente(models.Model):
	cod_client = models.IntegerField(primary_key=True)
	name = models.CharField('Nome', max_length=100)
	category = models.CharField('Categoria', max_length=100)
	cpf = models.CharField('CPF', max_length=11)
	rg = models.CharField('RG', max_length=11)
	cnh = models.CharField('CNH', max_length=11)
	titulo = models.CharField('Titulo de eleitor', max_length=11)
	certidao = models.CharField('Certidao de Nascimento', max_length=100)
	schooling = models.CharField('Esolaridade', max_length=20)
	professing = models.CharField('Profissão', max_length=20)
	date = models.DateField('Nascimento')
	appliance = models.CharField('Tipo de Aparelho', max_length=100)
	deficient = models.IntegerField('Número de Deficientes')
	income = models.FloatField('Renda Familiar')
	home = models.CharField('Tipo de Moradia', max_length=10)	

class Especialidade(models.Model):
	cod_esp = models.IntegerField(primary_key=True)	
	description = models.CharField('Descrição', max_length=100, null=True)

class Tipo_Atendimento(models.Model):
	cod_tipo_atendimento = models.IntegerField(primary_key=True)
	descricao = models.CharField('Descrição', max_length=100)	

class Usuario(models.Model):
	cod_user = models.IntegerField(primary_key=True)
	name = models.CharField('Nome', max_length=100)
	login = models.CharField('Login', max_length=10)
	password = models.CharField('Senha', max_length=10)	

class Profissoes(models.Model):
	cod_prof = 	models.IntegerField(primary_key=True)
	description = models.CharField(max_length=100)



class Perfis(models.Model):
	cod_perfil = models.IntegerField(primary_key=True)
	description = models.CharField('Descrição', max_length=100)
	age = models.IntegerField('Idade')
	sexo = models.CharField(max_length=10)
	escolaridade = models.CharField('Escolaridade', max_length=10)

class Empresa(models.Model):
	cod_emp = models.IntegerField(primary_key=True)
	razao = models.CharField('Razão Social', max_length=100)
	ramo = models.CharField('Ramo', max_length=100) 
	fantasia = models.CharField('Fantasia', max_length=100) 
	adress = models.TextField('Endereço')	 	


class Profissional(models.Model):
	cod_prof = models.IntegerField(primary_key=True)
	cod_esp = models.ForeignKey(Especialidade)
	name = models.CharField('Nome', max_length=100)
	adress = models.TextField('Endereco')
	phone = models.CharField('Telefone', max_length=11)
	email = models.EmailField('e-mail')
	date = models.DateField('Data de Nascimento')
	cart_professional = models.CharField('Cart .Profissional', max_length=100)


class Atendimento(models.Model):
	cod_atendimento = models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)
	cod_user = models.ForeignKey(Usuario)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()	

class Agendamento(models.Model):
	cod_agenda = models.IntegerField(primary_key=True)
	cod_atendimento = models.ForeignKey(Atendimento)
	cod_prof = models.ForeignKey(Profissional)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()	
	cliente = models.CharField('Cliente', max_length=100)
	profissional = models.CharField('Profissional', max_length=100)


class Tipo_Deficiencia(models.Model):
	cod_tipo_deficiencia = models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)
	description = models.CharField('Descrição', max_length=100)

class Cliente_Profissoes(models.Model):	
	cod_client_prof = models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)
	cod_prof = models.ForeignKey(Profissoes)

class Telefone(models.Model):	
	cod_telefone =	models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)
	cod_prof = models.ForeignKey(Profissional)
	cod_emp = models.ForeignKey(Empresa)
	phone = models.CharField('Telefone', max_length=11)

class Envio(models.Model):	
	cod_envio =	models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)
	cod_prof = models.ForeignKey(Profissional)
	cod_emp = models.ForeignKey(Empresa)
	email = models.EmailField()	

class Habilidade(models.Model):
	cod_hab = models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)	
	tipo = models.CharField('Tipo', max_length=100)
	description = models.CharField('Descrição', max_length=100)

class Tipo_Aparelho(models.Model):
	cod_tipo_aparelho = models.IntegerField(primary_key=True)
	cod_client = models.ForeignKey(Cliente)	
	description = models.CharField('Descrição', max_length=100)	

class Vaga(models.Model):
	cod_vagas = models.IntegerField(primary_key=True)
	cod_emp =  models.ForeignKey(Empresa)
	status = models.BooleanField()	
	date = models.DateField('Data de Inclusão')	








	



