# Generated by Django 3.0.3 on 2020-04-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_petition_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='approved',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]