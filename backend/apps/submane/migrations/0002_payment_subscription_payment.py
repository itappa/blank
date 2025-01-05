# Generated by Django 5.1.4 on 2025-01-03 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submane', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('CREDIT', 'クレジット'), ('BANK', '口座振替')], default='CREDIT', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='submane.payment'),
        ),
    ]