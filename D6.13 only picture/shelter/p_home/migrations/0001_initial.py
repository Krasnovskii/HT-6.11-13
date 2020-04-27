# Generated by Django 3.0.5 on 2020-04-21 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание животного')),
                ('date', models.DateField(verbose_name='Дата поступления')),
                ('type', models.CharField(max_length=100, verbose_name='Вид животного')),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=100, verbose_name='порода')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_home.Animal')),
            ],
        ),
    ]
