# Generated by Django 4.1.5 on 2023-01-30 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0022_remove_equipment_user_equipment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
