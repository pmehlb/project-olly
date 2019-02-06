# Generated by Django 2.0.4 on 2019-01-12 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_gamechoice_platformchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GameChoice', to='matches.GameChoice'),
        ),
        migrations.AlterField(
            model_name='match',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PlatformChoice', to='matches.PlatformChoice'),
        ),
    ]