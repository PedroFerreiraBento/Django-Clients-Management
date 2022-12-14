# Generated by Django 4.1.2 on 2022-10-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_alter_client_created_at_alter_client_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='clienthistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='relatedcnpj',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='relatedcnpj',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='relatedcnpjhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
    ]
