# Generated by Django 4.1.5 on 2023-02-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0032_leave_request_started_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='yearly_leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
