# Generated by Django 4.1.3 on 2022-12-30 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0007_alter_dishtype_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="dish_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="kitchen.dishtype",
            ),
        ),
    ]
