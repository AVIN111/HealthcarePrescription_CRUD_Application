# Generated by Django 3.1.5 on 2021-05-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('ENT', 'ENT'), ('Neurology', 'Neurology'), ('General OPD', 'General OPD'), ('Dental', 'Dental')], default='Unspecified', max_length=45)),
                ('mobile', models.CharField(default='-----', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('preconditions', models.CharField(choices=[('None', 'None'), ('Diabetes', 'Diabetes'), ('Asthma', 'Asthma'), ('Hypertension', 'Hypertension')], default='Unspecified', max_length=15)),
            ],
        ),
    ]
