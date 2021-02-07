# Generated by Django 3.1.6 on 2021-02-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksub', '0002_auto_20210205_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='number',
            field=models.CharField(max_length=12, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='ticker',
            field=models.CharField(max_length=10, verbose_name='Stock Ticker'),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('ticker', 'number')},
        ),
    ]