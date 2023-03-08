# Generated by Django 2.2.2 on 2019-08-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemPool', '0009_auto_20190804_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papercontent',
            name='content',
            field=models.TextField(max_length=400, verbose_name='试题ID列表'),
        ),
        migrations.AlterField(
            model_name='papertemplate',
            name='typeFourScore',
            field=models.DecimalField(decimal_places=1, default=20, max_digits=3, verbose_name='综合应用题分值'),
        ),
        migrations.AlterField(
            model_name='papertemplate',
            name='typeThreeScore',
            field=models.DecimalField(decimal_places=1, default=12.5, max_digits=3, verbose_name='简单应用题分值'),
        ),
        migrations.AlterField(
            model_name='papertemplate',
            name='typeTwoScore',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=3, verbose_name='基本操作题分值'),
        ),
        migrations.AlterField(
            model_name='testitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='picssss', verbose_name='试题图片'),
        ),
    ]