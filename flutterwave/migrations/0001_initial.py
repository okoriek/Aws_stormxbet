# Generated by Django 4.0 on 2022-12-19 20:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlutterWave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=1000000)),
                ('email', models.EmailField(blank=True, max_length=3000, null=True)),
                ('reference', models.CharField(max_length=200, unique=True)),
                ('generated', models.DateTimeField(default=django.utils.timezone.now)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-generated',),
            },
        ),
    ]