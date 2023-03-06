# Generated by Django 4.1.7 on 2023-03-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_remove_task_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/", verbose_name="Изображение"
            ),
        ),
    ]