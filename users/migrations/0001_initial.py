# Generated by Django 4.2.6 on 2023-10-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('_id', models.UUIDField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField()),
            ],
        ),
    ]