# Generated by Django 3.1 on 2020-10-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='delprice',
            field=models.FloatField(default=0, verbose_name=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0, verbose_name=10),
            preserve_default=False,
        ),
    ]
