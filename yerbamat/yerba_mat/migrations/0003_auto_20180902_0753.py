# Generated by Django 2.1.1 on 2018-09-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yerba_mat', '0002_auto_20180901_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='pictures/None/no-img.jpg', upload_to='pictures/', verbose_name='pictures'),
        ),
    ]
