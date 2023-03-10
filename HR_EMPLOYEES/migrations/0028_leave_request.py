# Generated by Django 4.1.5 on 2023-01-31 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0027_weakly_leave_alter_equipment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_days_requested', models.IntegerField(null=True)),
                ('accepted', models.BooleanField()),
                ('the_leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_EMPLOYEES.daysoff')),
            ],
        ),
    ]
