# Generated by Django 4.2.13 on 2024-06-03 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_order"),
    ]

    operations = [
        migrations.RenameField(model_name="order", old_name="Total", new_name="total",),
        migrations.RemoveField(model_name="order", name="image",),
        migrations.RemoveField(model_name="order", name="name",),
        migrations.RemoveField(model_name="order", name="price",),
        migrations.AddField(
            model_name="order",
            name="coffee",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="authentication.coffee",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
