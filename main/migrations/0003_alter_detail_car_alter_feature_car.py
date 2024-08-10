# Generated by Django 5.1 on 2024-08-10 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_detail_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='main.car'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature', to='main.car'),
        ),
    ]
