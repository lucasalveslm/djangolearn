# Generated by Django 2.2.5 on 2019-09-12 16:28

from django.db import migrations, models
import polls.utils


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=polls.utils.get_datetime_with_timezone, verbose_name='date published'),
        ),
    ]
