# Generated by Django 3.1 on 2020-09-03 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_paciente'),
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='users.paciente'),
        ),
    ]
