# Generated by Django 2.2.7 on 2020-07-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='Canada', max_length=64),
            preserve_default=False,
        ),
    ]