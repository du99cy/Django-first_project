# Generated by Django 4.1.3 on 2022-11-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container_type', '0002_alter_containertype_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containertype',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='containertype',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
    ]