# Generated by Django 4.1.4 on 2023-04-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('gender', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('course', models.TextField(max_length=50)),
                ('address', models.TextField(max_length=50)),
            ],
        ),
    ]
