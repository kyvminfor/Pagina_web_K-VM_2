# Generated by Django 4.2.1 on 2024-01-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('motivo_contacto', models.CharField(max_length=400)),
                ('forma_contacto', models.CharField(choices=[('telefono', 'Comunicarse por teléfono'), ('email', 'Comunicarse por email')], max_length=20)),
            ],
        ),
    ]
