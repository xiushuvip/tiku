# Generated by Django 2.2.2 on 2019-08-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemPool', '0004_auto_20190803_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='./static/pics', verbose_name='试题图片'),
        ),
    ]
