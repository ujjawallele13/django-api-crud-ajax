# Generated by Django 4.2.1 on 2023-05-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id", models.IntegerField()),
                ("product_name", models.CharField(max_length=255)),
                ("introduction_date", models.DateField()),
                ("url", models.URLField()),
            ],
        ),
    ]
