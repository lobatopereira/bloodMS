# Generated by Django 3.2.9 on 2022-08-19 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodstock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_package', models.IntegerField(blank=True, null=True)),
                ('bloodGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloodstock.bloodgroup')),
            ],
        ),
    ]
