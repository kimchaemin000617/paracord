# Generated by Django 4.0.1 on 2022-01-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
