# Generated by Django 3.1.5 on 2022-01-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220116_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='identifier',
            field=models.CharField(default='PABCK9391W', max_length=500),
        ),
    ]
