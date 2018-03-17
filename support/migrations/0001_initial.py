# Generated by Django 2.0.1 on 2018-03-06 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('category', models.SmallIntegerField(choices=[(0, 'General'), (1, 'Prize Claim'), (2, 'Tournament Support'), (3, 'Billing'), (4, 'Refund Request'), (5, 'PSN/XBL Issues'), (6, 'Match Support/Dispute')], default=0)),
                ('text', models.TextField(default='A detailed description of your issue')),
                ('status', models.SmallIntegerField(choices=[(0, 'New'), (1, 'On Hold'), (2, 'In Progress'), (3, 'Resolved'), (4, 'Closed')], default=0)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL, verbose_name='assignee')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_create', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='support.Ticket', verbose_name='Ticket')),
            ],
            options={
                'verbose_name': 'Ticket comment',
                'verbose_name_plural': 'Ticket comments',
                'ordering': ['date'],
            },
        ),
    ]
