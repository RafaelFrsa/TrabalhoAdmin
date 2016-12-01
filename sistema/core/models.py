from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Cliente(models.Model):

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

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'
		ordering = ('-name',)

	def __str__(self):
		return self.name


class Especialidade(models.Model):
	
	description = models.CharField('Descrição', max_length=100, null=True)

	class Meta:
		verbose_name='Especialidade'
		verbose_name_plural='Especialidades'

	def __str__(self):
		return self.description


	
class Tipo_Atendimento(models.Model):
	
	description = models.CharField('Descrição', max_length=100)	

	class Meta:
		verbose_name='Tipo Atendimento'
		verbose_name_plural='Tipo Atendimentos'

	def __str__(self):
		return self.description


class Usuario(models.Model):
	
	name = models.CharField('Nome', max_length=100)
	login = models.CharField('Login', max_length=10)
	password = models.CharField('Senha', max_length=10)	

	class Meta:
		verbose_name='Usuario'
		verbose_name_plural='Usuarios'
		ordering = ('-name',)

	def __str__(self):
		return self.name


class Profissao(models.Model):
	

	description = models.CharField( max_length=100)

	class meta:
		verbose_name='Profissão'
		verbose_name_plural='Profissões'

	def __str__(self):
		return self.description


class Perfis(models.Model):
	
	description = models.CharField('Descrição', max_length=100)
	age = models.IntegerField('Idade')
	sexo = models.CharField(max_length=10)
	escolaridade = models.CharField('Escolaridade', max_length=10)

	class Meta:
		verbose_name='Perfil'
		verbose_name_plural='Perfis'


	def __str__(self):
		return self.description


class Empresa(models.Model):
	
	razao = models.CharField('Razão Social', max_length=100)
	ramo = models.CharField('Ramo', max_length=100) 
	fantasia = models.CharField('Fantasia', max_length=100) 
	adress = models.TextField('Endereço')	

	class Meta:
		verbose_name='Empresa'
		verbose_name_plural='Empresas'
 	
	def __str__(self):
		return self.fantasia


class Profissional(models.Model):
	
	cod_esp = models.ForeignKey('Especialidade')
	name = models.CharField('Nome', max_length=100)
	adress = models.TextField('Endereco')
	phone = models.CharField('Telefone', max_length=11)
	email = models.EmailField('e-mail')
	date = models.DateField('Data de Nascimento')
	cart_professional = models.CharField('Cart .Profissional', max_length=100)

	class Meta:
		verbose_name='Profissional'
		verbose_name_plural='Profissionais'
		ordering = ('-name',)

	def __str__(self):
		return self.name


class Atendimento(models.Model):
	
	cod_client = models.ForeignKey('Cliente')
	cod_user = models.ForeignKey('Usuario')
	published_date = models.DateTimeField(
            blank=True, null=True)

	class Meta:
		verbose_name='Atendimento'
		verbose_name_plural='Atendimentos'

	

	def publish(self):
		self.published_date = timezone.now()
		self.save()	

class Agendamento(models.Model):
	
	cod_cliente = models.ForeignKey('Cliente')
	cod_atendimento = models.ForeignKey('Atendimento')
	cod_prof = models.ForeignKey('Profissional')
	published_date = models.DateTimeField(
            blank=True, null=True)

	class Meta:
		verbose_name='Agendamento'
		verbose_name_plural='Agendamentos'

	def __str__(self):
		return self.cod_cliente.name
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()	
	cliente = models.CharField('Cliente', max_length=100)
	profissional = models.CharField('Profissional', max_length=100)


class Tipo_Deficiencia(models.Model):

	cod_client = models.ForeignKey('Cliente')
	description = models.CharField('Descrição', max_length=100)

	class Meta:
		verbose_name='Tipo Deficiencia'
		verbose_name_plural='Tipo Deficiencias'

	def __str__(self):
		return self.description
	

class Cliente_Profissoes(models.Model):	

	cod_client = models.ForeignKey('Cliente')
	cod_prof = models.ForeignKey('Profissao')

	class Meta:
		verbose_name='Cliente Profissao'
		verbose_name_plural='Cliente Profissoes'
	

class Telefone(models.Model):	

	cod_client = models.ForeignKey('Cliente')
	cod_prof = models.ForeignKey('Profissional')
	cod_emp = models.ForeignKey('Empresa')
	phone = models.CharField('Telefone', max_length=11)

	class Meta:
		verbose_name='Telefone'
		verbose_name_plural='Telefones'

	def __str__(self):
		return self.phone
	
	

class Envio(models.Model):	
	
	cod_client = models.ForeignKey('Cliente')
	cod_prof = models.ForeignKey('Profissional')
	cod_emp = models.ForeignKey('Empresa')
	email = models.EmailField()	

	class Meta:
		verbose_name='Envio'
		verbose_name_plural='Envios'
	


class Habilidade(models.Model):

	cod_client = models.ForeignKey('Cliente')	
	tipo = models.CharField('Tipo', max_length=100)
	description = models.CharField('Descrição', max_length=100)

	class Meta:
		verbose_name='Habilidade'
		verbose_name_plural='Habilidades'
	
	def __str__(self):
		return self.description
	

class Tipo_Aparelho(models.Model):
	
	cod_client = models.ForeignKey('Cliente')	
	description = models.CharField('Descrição', max_length=100)	

	class Meta:
		verbose_name='Tipo Aparelho'
		verbose_name_plural='Tipo Aparelhos'

	def __str__(self):
		return self.description
	
	

class Vaga(models.Model):

	cod_emp =  models.ForeignKey('Empresa')
	status = models.BooleanField()	
	date = models.DateField('Data de Inclusão')	

	class Meta:
		verbose_name='Vaga'
		verbose_name_plural='Vagas'
	








	



