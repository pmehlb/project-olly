# Generated by Django 2.1.5 on 2019-02-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0009_auto_20190206_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticinfo',
            name='welcomeln1',
            field=models.CharField(blank=True, default='welcome1', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='staticinfo',
            name='welcomeln2',
            field=models.CharField(blank=True, default='welcome2', max_length=25, null=True),
        ),
    ]