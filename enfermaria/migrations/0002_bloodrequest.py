# Generated by Django 3.2.9 on 2022-08-19 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enfermaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=10)),
                ('date_of_request', models.DateField(null=True, verbose_name='Data Pedidu')),
                ('is_locked', models.BooleanField(blank=True, default=False, null=True)),
                ('is_sent', models.BooleanField(blank=True, default=False, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('is_rejected', models.BooleanField(blank=True, default=False, null=True)),
                ('rejected_info', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('enfermaria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enfermaria.enfermaria')),
            ],
        ),
    ]