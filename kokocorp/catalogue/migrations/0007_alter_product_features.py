# Generated by Django 3.2.5 on 2021-07-12 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.TextField(max_length=250),
        ),
    ]
