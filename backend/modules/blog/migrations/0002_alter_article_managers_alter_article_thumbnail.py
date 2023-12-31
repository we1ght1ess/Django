# Generated by Django 4.2.7 on 2023-11-21 14:24

import django.core.validators
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('custom', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images/thumbnails/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Превью поста'),
        ),
    ]
