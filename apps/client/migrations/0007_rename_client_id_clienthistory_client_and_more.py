# Generated by Django 4.1.2 on 2022-10-24 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_clienthistory_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clienthistory',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='relatedcnpjhistory',
            old_name='relatedcnpj_id',
            new_name='relatedcnpj',
        ),
    ]
