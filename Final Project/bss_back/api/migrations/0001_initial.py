# Generated by Django 2.2 on 2022-05-04 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('image', models.CharField(max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('link_to_product', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
    ]
