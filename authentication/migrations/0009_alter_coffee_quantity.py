# Generated by Django 4.2.13 on 2024-06-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0008_coffee_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffee", name="quantity", field=models.IntegerField(),
        ),
    ]
