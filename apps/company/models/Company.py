from django.db import models
from . import StatusCompany, PaymentStatusCompany

class Company(models.Model):
    brand_name = models.CharField(verbose_name='Nome Fantasia', max_length=255, null=False, blank=False)
    corporate_name = models.CharField(verbose_name='Razão Social', max_length=255, null=False, blank=False)
    document = models.CharField(verbose_name='CPF/CNPJ', max_length=50, unique=True, null=False, blank=False)
    ie = models.CharField(verbose_name='Inscrição Estadual', max_length=50, unique=True, null=True, blank=True)
    postal_code = models.CharField(verbose_name='CEP', max_length=20, null=True, blank=True)
    state = models.CharField(verbose_name='Estado', max_length=10, null=True, blank=True)
    city = models.CharField(verbose_name='Cidade', max_length=100, null=True, blank=True)
    district = models.CharField(verbose_name='Bairro', max_length=100, null=True, blank=True)
    street = models.CharField(verbose_name='Endereço', max_length=255, null=True, blank=True)
    number = models.CharField(verbose_name='Número', max_length=10, null=True, blank=True)
    phone = models.CharField(verbose_name='Telefone', max_length=20, null=True, blank=True)
    cell_phone = models.CharField(verbose_name='Celular', max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name='E-mail', max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(verbose_name='Senha',max_length=255, null=False, blank=False)
    slugify = models.SlugField(verbose_name='Slug', null=False, blank=False)
    primary_color = models.CharField(verbose_name='Cor Primaria', max_length=50, null=False, blank=False)
    secondary_color = models.CharField(verbose_name='Cor Secundaria', max_length=50, null=False, blank=False)
    status = models.IntegerField(verbose_name='Status', choices=StatusCompany.choices, default=StatusCompany.ATIVO, null=False, blank=False)
    payment_status = models.IntegerField(verbose_name='Status Pagamento', choices=PaymentStatusCompany.choices, default=PaymentStatusCompany.PAGO, null=False, blank=False)
    observation = models.TextField(verbose_name='Orservação', null=True, blank=True)
    terms = models.TextField(verbose_name='Termos', null=True, blank=True)