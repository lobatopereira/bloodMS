# Generated by Django 3.2.9 on 2022-09-17 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enfermaria', '0008_bloodrequest_is_respond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='package',
            field=models.IntegerField(null=True, verbose_name='Total Pakote Ran'),
        ),
        migrations.AlterField(
            model_name='bloodrequestresponse',
            name='bloodRequest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloodrequestresponse', to='enfermaria.bloodrequest'),
        ),
    ]
