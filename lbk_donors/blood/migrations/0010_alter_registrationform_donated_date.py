# Generated by Django 5.0 on 2024-03-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0009_alter_registrationform_donated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='donated_date',
            field=models.CharField(max_length=20),
        ),
    ]
