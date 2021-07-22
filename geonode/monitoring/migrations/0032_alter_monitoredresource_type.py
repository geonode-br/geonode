# Generated by Django 3.2.4 on 2021-07-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0031_auto_20201012_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoredresource',
            name='type',
            field=models.CharField(choices=[('', 'No resource'), ('layer', 'Dataset'), ('map', 'Map'), ('resource_base', 'Resource base'), ('document', 'Document'), ('style', 'Style'), ('admin', 'Admin'), ('url', 'URL'), ('other', 'Other')], default='', max_length=255),
        ),
    ]
