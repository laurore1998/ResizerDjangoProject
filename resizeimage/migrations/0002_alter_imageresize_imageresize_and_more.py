# Generated by Django 4.1 on 2022-09-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizeimage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageresize',
            name='imageresize',
            field=models.FileField(blank=True, null=True, upload_to='static/dosye_foto/'),
        ),
        migrations.AlterField(
            model_name='imageresize',
            name='imagesubmit',
            field=models.FileField(blank=True, null=True, upload_to='static/dosye_foto/'),
        ),
    ]
