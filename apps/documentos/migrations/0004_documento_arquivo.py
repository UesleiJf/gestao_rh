# Generated by Django 2.1.7 on 2019-03-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20190306_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
