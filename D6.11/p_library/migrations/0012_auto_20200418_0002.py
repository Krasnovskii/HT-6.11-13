# Generated by Django 3.0.5 on 2020-04-18 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_auto_20200417_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='picture',
            new_name='images',
        ),
    ]
