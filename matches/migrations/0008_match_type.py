# Generated by Django 2.1.7 on 2019-05-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20190112_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]