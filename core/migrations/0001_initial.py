# Generated by Django 4.2.1 on 2023-05-09 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.FloatField()),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("RUB", "Russian Ruble"),
                            ("EUR", "Euro"),
                            ("USD", "US Dollar"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seller",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("finished", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.customer"
                    ),
                ),
                ("items", models.ManyToManyField(to="core.item")),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.seller"
            ),
        ),
    ]
