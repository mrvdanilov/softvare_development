# Generated by Django 3.1.4 on 2021-01-10 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
            ],
        ),
    ]
