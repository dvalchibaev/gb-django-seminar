# Generated by Django 4.2.4 on 2023-09-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("publications_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="publications_app.article",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="publications_app.author",
            ),
        ),
    ]
