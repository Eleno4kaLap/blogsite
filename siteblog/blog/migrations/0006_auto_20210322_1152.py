# Generated by Django 3.1.4 on 2021-03-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_emailsubscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscriptions',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
