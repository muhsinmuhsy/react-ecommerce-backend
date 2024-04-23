# Generated by Django 4.1 on 2024-04-23 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.size'),
        ),
    ]