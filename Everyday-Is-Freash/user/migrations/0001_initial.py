# Generated by Django 2.1.3 on 2018-12-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('u_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=10)),
                ('addr', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]