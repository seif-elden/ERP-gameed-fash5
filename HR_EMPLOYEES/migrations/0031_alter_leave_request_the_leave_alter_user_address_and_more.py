# Generated by Django 4.1.5 on 2023-02-01 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0030_alter_leave_request_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_request',
            name='the_leave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_leave', to='HR_EMPLOYEES.daysoff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HR_EMPLOYEES.branches'),
        ),
        migrations.AlterField(
            model_name='user',
            name='caontact_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='direct_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergancy_contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='family_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='family_relation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='the_contract_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
