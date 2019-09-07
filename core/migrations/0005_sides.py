# Generated by Django 2.2.4 on 2019-09-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190903_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Basliq')),
                ('desc', models.TextField(verbose_name='Metni daxil edin')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sides', verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('url', models.CharField(max_length=50, verbose_name='URL')),
                ('contact_email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'sides',
                'verbose_name_plural': 'sidess',
            },
        ),
    ]
