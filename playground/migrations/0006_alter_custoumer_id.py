# Generated by Django 4.2.7 on 2023-11-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_custoumer_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custoumer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
