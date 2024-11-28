# Generated by Django 4.1 on 2024-11-27 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]