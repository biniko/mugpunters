# Generated by Django 4.1.3 on 2022-11-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0007_alter_team_logo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
