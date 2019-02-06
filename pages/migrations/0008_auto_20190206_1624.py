# Generated by Django 2.0.10 on 2019-02-06 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20190206_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticinfo',
            name='facebookpage',
            field=models.URLField(blank=True, null=True, verbose_name='facebook_page'),
        ),
        migrations.AlterField(
            model_name='staticinfo',
            name='instagrampage',
            field=models.URLField(blank=True, null=True, verbose_name='instagram_page'),
        ),
        migrations.AlterField(
            model_name='staticinfo',
            name='twitchchannel',
            field=models.URLField(blank=True, null=True, verbose_name='twitch_channel'),
        ),
        migrations.AlterField(
            model_name='staticinfo',
            name='twitterprofile',
            field=models.URLField(blank=True, null=True, verbose_name='twitter_profile'),
        ),
        migrations.AlterField(
            model_name='staticinfo',
            name='youtubechannel',
            field=models.URLField(blank=True, null=True, verbose_name='youtube_channel'),
        ),
    ]