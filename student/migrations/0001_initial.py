# Generated by Django 3.2.6 on 2022-08-27 16:45

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
                ('roll_no', models.TextField()),
                ('name', models.TextField(max_length=40)),
                ('stud_class', models.TextField()),
                ('department', models.TextField()),
            ],
        ),
    ]
