# Generated by Django 5.0.2 on 2024-05-09 12:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catagory',
            options={'ordering': ('name',), 'verbose_name_plural': 'Catagories'},
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='items_images')),
                ('is_sold', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.catagory')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
