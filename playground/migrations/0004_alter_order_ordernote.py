# Generated by Django 4.2.6 on 2023-10-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_alter_cars_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderNote',
            field=models.CharField(max_length=500, null=True),
        ),
    ]