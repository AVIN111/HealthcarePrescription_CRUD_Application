# Generated by Django 3.1.5 on 2021-05-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_register', '0004_patient_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('O', 'Others'), ('M', 'Male'), ('F', 'Female')], default='Unspecified', max_length=100),
        ),
    ]
