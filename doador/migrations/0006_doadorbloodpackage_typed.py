# Generated by Django 3.2.9 on 2022-10-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doador', '0005_alter_doadorbloodpackage_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='doadorbloodpackage',
            name='typeD',
            field=models.CharField(blank=True, choices=[('Voluntariu', 'Voluntariu'), ('Subtituisaun', 'Subtituisaun')], default='Voluntariu', max_length=30, null=True),
        ),
    ]
