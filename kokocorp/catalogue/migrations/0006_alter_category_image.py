# Generated by Django 3.2.4 on 2021-07-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category'),
        ),
    ]
