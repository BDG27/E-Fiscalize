# Generated by Django 4.1.5 on 2023-01-22 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Nome Fantasia')),
                ('corporate_name', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('document', models.CharField(max_length=50, unique=True, verbose_name='CPF/CNPJ')),
                ('ie', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Inscrição Estadual')),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='CEP')),
                ('state', models.CharField(blank=True, max_length=10, null=True, verbose_name='Estado')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
                ('number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('cell_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=255, verbose_name='Senha')),
                ('slugify', models.SlugField(verbose_name='Slug')),
                ('primary_color', models.CharField(max_length=50, verbose_name='Cor Primaria')),
                ('secondary_color', models.CharField(max_length=50, verbose_name='Cor Secundaria')),
                ('status', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Inativo')], default=1, verbose_name='Status')),
                ('payment_status', models.IntegerField(choices=[(1, 'Pago'), (2, 'Aguardando Pagamento')], default=1, verbose_name='Status Pagamento')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='Orservação')),
                ('terms', models.TextField(blank=True, null=True, verbose_name='Termos')),
            ],
        ),
    ]