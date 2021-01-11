# Generated by Django 3.0.6 on 2020-12-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamsoft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.CharField(max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=255, verbose_name=''),
        ),
    ]