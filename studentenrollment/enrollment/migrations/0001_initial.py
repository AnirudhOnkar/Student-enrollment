# Generated by Django 5.0.6 on 2024-07-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]