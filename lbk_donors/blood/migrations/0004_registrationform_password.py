# Generated by Django 5.0 on 2024-03-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_registrationform_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='password',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
