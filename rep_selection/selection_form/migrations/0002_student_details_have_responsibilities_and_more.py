# Generated by Django 5.0.3 on 2024-03-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='have_responsibilities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student_details',
            name='select',
            field=models.BooleanField(default=False),
        ),
    ]
