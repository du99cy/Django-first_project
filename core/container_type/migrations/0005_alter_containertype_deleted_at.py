# Generated by Django 4.1.3 on 2022-11-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container_type', '0004_alter_containertype_deleted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containertype',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]