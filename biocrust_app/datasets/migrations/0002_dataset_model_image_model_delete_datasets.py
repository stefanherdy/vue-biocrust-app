# Generated by Django 4.2.4 on 2023-09-12 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dataset_Model",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255)),
                ("slug", models.SlugField()),
                ("dataset_created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-dataset_created",),
            },
        ),
        migrations.CreateModel(
            name="Image_Model",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255)),
                ("slug", models.SlugField()),
                ("description", models.TextField(blank=True, null=True)),
                ("img", models.ImageField(upload_to="images/")),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="images/")),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dataset",
                        to="datasets.dataset_model",
                    ),
                ),
            ],
            options={
                "ordering": ("-date_added",),
            },
        ),
        migrations.DeleteModel(
            name="datasets",
        ),
    ]
