# Generated by Django 4.2.5 on 2023-12-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_of_computer_app', '0007_alter_casefanfeature_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]