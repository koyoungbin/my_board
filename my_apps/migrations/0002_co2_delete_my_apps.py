# Generated by Django 4.2.5 on 2023-09-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CO2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average', models.FloatField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.DeleteModel(
            name='my_apps',
        ),
    ]