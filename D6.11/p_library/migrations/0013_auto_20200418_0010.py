# Generated by Django 3.0.5 on 2020-04-18 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_auto_20200418_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='images',
            new_name='picture',
        ),
    ]