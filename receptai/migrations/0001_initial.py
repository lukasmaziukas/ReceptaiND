# Generated by Django 4.0.3 on 2022-03-20 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Koks receptuko vardelis?', max_length=100, verbose_name='Pavadinimas')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receptas',
                'verbose_name_plural': 'Receptai',
            },
        ),
        migrations.CreateModel(
            name='Produktas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Įrašyk produktą', max_length=300, verbose_name='Produktas')),
                ('isCompleted', models.BooleanField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptai.receptas')),
            ],
            options={
                'verbose_name': 'Produktas',
                'verbose_name_plural': 'Produktai',
            },
        ),
    ]
