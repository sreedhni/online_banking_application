# Generated by Django 5.0.4 on 2024-05-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0008_remove_loantype_loan_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbranches',
            name='has_account',
            field=models.BooleanField(default=False),
        ),
    ]