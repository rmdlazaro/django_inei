# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-02 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=11)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='PlanEstudios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('anho', models.IntegerField()),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Especialidad')),
            ],
        ),
        migrations.AddField(
            model_name='especialidad',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Facultad'),
        ),
        migrations.AddField(
            model_name='curso',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.PlanEstudios'),
        ),
        migrations.AddField(
            model_name='aula',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Local'),
        ),
    ]
