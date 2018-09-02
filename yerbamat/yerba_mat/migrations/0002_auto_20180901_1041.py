# Generated by Django 2.1.1 on 2018-09-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yerba_mat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='pictures/None/no-img.jpg', upload_to='pictures', verbose_name='pictures'),
        ),
    ]
