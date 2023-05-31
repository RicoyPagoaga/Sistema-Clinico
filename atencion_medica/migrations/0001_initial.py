# Generated by Django 4.0.6 on 2022-07-18 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('NoConsultorio', models.AutoField(primary_key=True, serialize=False)),
                ('Jornada', models.CharField(max_length=70)),
                ('Piso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('NoDepto', models.AutoField(primary_key=True, serialize=False)),
                ('Especialidad', models.CharField(max_length=100)),
                ('concentracion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('DNI', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('FechaNac', models.DateField()),
                ('Telefono', models.CharField(max_length=8)),
                ('correo', models.CharField(max_length=254)),
                ('Direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('IdDoctor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('FechaNac', models.DateField()),
                ('Telefono', models.CharField(max_length=8)),
                ('correo', models.CharField(max_length=254)),
                ('FechaIngreso', models.DateField()),
                ('NoConsultorio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atencion_medica.consultorio')),
            ],
        ),
        migrations.AddField(
            model_name='consultorio',
            name='NoDepto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atencion_medica.departamento'),
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('NoCita', models.AutoField(primary_key=True, serialize=False)),
                ('FechaRegistro', models.DateField()),
                ('FechaAtencion', models.DateTimeField()),
                ('Descripcion', models.CharField(max_length=200)),
                ('DniPaciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atencion_medica.paciente')),
                ('IdDoctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atencion_medica.doctor')),
            ],
        ),
    ]