from django.contrib import admin
from sistema.core.models import Especialidade, Tipo_Atendimento, Usuario, Profissao, Cliente,\
 Perfis, Empresa, Profissional, Agendamento, Atendimento, Tipo_Deficiencia, Cliente_Profissoes, \
 Telefone, Envio, Habilidade, Tipo_Aparelho, Vaga
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):

	list_display=['name']
	list_filter=['name']
	search_fields=['name']

	
class EspecialidadeAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']	

class Tipo_AtendimentoAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']	

class UsuarioAdmin(admin.ModelAdmin):

	list_display=['name']
	list_filter=['name']
	search_fields=['name']	

class ProfissaoAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']	

class PerfisAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']	

class EmpresaAdmin(admin.ModelAdmin):

	list_display=['fantasia']
	list_filter=['fantasia']
	search_fields=['fantasia']		
	
class ProfissionalAdmin(admin.ModelAdmin):

	list_display=['name']
	list_filter=['name']
	search_fields=['name']	

class AgendamentoAdmin(admin.ModelAdmin):

	list_display=['published_date']
	list_filter=['published_date']
	search_fields=['published_date']

	actions = ['envia_confirmacao']


	def envia_confirmacao(self, request, queryset):
		count = 0
		for dados in queryset:
			#dados = queryset[0]
			body = render_to_string('envio.txt', {'dados': dados})
			count+=1
			mail.send_mail('Confirmação de Agendamento.', body, settings.DEFAULT_FROM_EMAIL, 
				[settings.DEFAULT_FROM_EMAIL, 'local@gmail.com'])

		if count == 1:
			msg = 'Email enviado com sucesso!'
		else:
			msg = 'Emails enviados com sucesso!'

		# Exibe mensagem de confirmação na interface de administração
		self.message_user(request, msg.format(count))

	envia_confirmacao.short_description = 'Enviar Email de Confirmação'


class AtendimentoAdmin(admin.ModelAdmin):

	list_display=['published_date']
	list_filter=['published_date']
	search_fields=['published_date']

class Tipo_DeficienciaAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']

class TelefoneAdmin(admin.ModelAdmin):

	list_display=['phone']
	list_filter=['phone']
	search_fields=['phone']		

class EnvioAdmin(admin.ModelAdmin):

	list_display=['email']
	list_filter=['email']
	search_fields=['email']	

class HabilidadeAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']		

class Tipo_AparelhoAdmin(admin.ModelAdmin):

	list_display=['description']
	list_filter=['description']
	search_fields=['description']	

class VagaAdmin(admin.ModelAdmin):

	list_display=['date']
	list_filter=['date']
	search_fields=['date']				

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Tipo_Atendimento, Tipo_AtendimentoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Profissao, ProfissaoAdmin)
admin.site.register(Perfis, PerfisAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Profissional,ProfissionalAdmin)
admin.site.register(Agendamento,AgendamentoAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
admin.site.register(Tipo_Deficiencia, Tipo_DeficienciaAdmin)
admin.site.register(Cliente_Profissoes)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Envio, EnvioAdmin)
admin.site.register(Habilidade, HabilidadeAdmin)
admin.site.register(Tipo_Aparelho, Tipo_AparelhoAdmin)
admin.site.register(Vaga, VagaAdmin)





