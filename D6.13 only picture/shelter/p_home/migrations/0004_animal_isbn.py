# Generated by Django 3.0.5 on 2020-04-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_home', '0003_auto_20200421_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='ISBN',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]
