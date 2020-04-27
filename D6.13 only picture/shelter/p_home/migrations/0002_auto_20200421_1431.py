# Generated by Django 3.0.5 on 2020-04-21 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='animal',
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='p_home.Breed'),
            preserve_default=False,
        ),
    ]