# Generated by Django 4.1.5 on 2023-01-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0008_alter_user_contract_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ProfileImg',
            field=models.ImageField(null=True, upload_to='images/uploads/'),
        ),
    ]
