# Generated by Django 3.2.6 on 2021-10-08 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_rename_product_name_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='used',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
    ]