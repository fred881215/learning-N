# Generated by Django 2.2.12 on 2020-08-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0002_auto_20200803_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercare',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
