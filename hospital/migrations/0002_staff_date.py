# Generated by Django 5.0.2 on 2024-04-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01'),
            preserve_default=False,
        ),
    ]
