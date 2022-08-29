# Generated by Django 3.2.15 on 2022-08-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_appointment_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='color',
            field=models.CharField(choices=[('0', '15:30 - 15:45'), ('1', '15:45 - 16:00'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
    ]
