# Generated by Django 5.0.4 on 2024-05-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_failed_login_attempts_user_last_failed_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_loan',
            field=models.BooleanField(default=False),
        ),
    ]
