# Generated by Django 3.1.5 on 2021-02-03 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210202_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='long_description',
            field=models.TextField(),
        ),
    ]