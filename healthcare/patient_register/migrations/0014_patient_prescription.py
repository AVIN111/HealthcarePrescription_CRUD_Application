# Generated by Django 3.1.5 on 2021-05-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_register', '0013_remove_patient_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='prescription',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
