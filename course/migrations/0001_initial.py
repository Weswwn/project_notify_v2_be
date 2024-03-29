# Generated by Django 3.0.7 on 2020-07-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectCode', models.CharField(max_length=4)),
                ('subjectNumber', models.CharField(max_length=4)),
                ('sectionNumber', models.CharField(max_length=4)),
            ],
            options={
                'unique_together': {('subjectCode', 'subjectNumber', 'sectionNumber')},
            },
        ),
    ]
