# Generated by Django 4.0 on 2023-06-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0016_alter_banners_imagen_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(upload_to='fotos/banners'),
        ),
    ]
