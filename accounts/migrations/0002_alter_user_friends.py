# Generated by Django 3.2.9 on 2022-02-09 10:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_accounts_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]