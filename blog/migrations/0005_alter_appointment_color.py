# Generated by Django 3.2.15 on 2022-08-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_appointment_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='color',
            field=models.CharField(choices=[('0', '15:30 - 15:45'), ('1', '15:45 - 16:00'), ('2', '16:00 - 16:15'), ('3', '16:15 - 16:30'), ('4', '16:30 - 16:45'), ('5', '16:45 - 17:00')], default='green', max_length=6),
        ),
    ]