# Generated by Django 2.2.15 on 2020-12-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20201209_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='bestof',
            field=models.SmallIntegerField(choices=[(1, 'Best of 1'), (2, 'Best of 2'), (3, 'Best of 3'), (4, 'Best of 4'), (5, 'Best of 5')], default=1),
        ),
    ]