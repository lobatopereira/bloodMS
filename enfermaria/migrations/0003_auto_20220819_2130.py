# Generated by Django 3.2.9 on 2022-08-19 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enfermaria', '0002_bloodrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='user_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_request', to=settings.AUTH_USER_MODEL),
        ),
    ]
