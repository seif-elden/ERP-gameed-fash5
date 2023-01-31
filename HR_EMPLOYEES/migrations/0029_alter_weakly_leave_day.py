# Generated by Django 4.1.5 on 2023-01-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0028_leave_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weakly_leave',
            name='day',
            field=models.CharField(choices=[('سبت', 'سبت'), ('أحد', 'أحد'), ('اثنين', 'اثنين'), ('ثلثاء', 'ثلثاء'), ('اربعاء', 'اربعاء'), ('خميس', 'خميس'), ('جمعه', 'جمعه')], max_length=10, unique=True),
        ),
    ]
