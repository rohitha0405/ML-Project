# Generated by Django 2.0.13 on 2020-08-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RetinopathyofPrematureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gestationalweek', models.CharField(max_length=100)),
                ('mechanicalventilation', models.CharField(max_length=100)),
                ('bloodtransfusion', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('lateonsetsepsis', models.CharField(max_length=100)),
                ('chorioamnionitis', models.CharField(max_length=100)),
                ('pretermprematureruptureofmembranes', models.CharField(max_length=100)),
                ('antenatalsteroidtherapy', models.CharField(max_length=100)),
                ('respiratorydistresssyndrome', models.CharField(max_length=100)),
                ('dopamindobutamin', models.CharField(max_length=100)),
                ('necrotizingenterocolitis', models.CharField(max_length=100)),
                ('intraventricularhemorrhage', models.CharField(max_length=100)),
                ('constant', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ROPTable',
            },
        ),
    ]