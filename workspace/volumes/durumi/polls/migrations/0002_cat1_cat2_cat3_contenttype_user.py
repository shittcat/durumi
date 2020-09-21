# Generated by Django 3.0.4 on 2020-08-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat1',
            fields=[
                ('cat1Id', models.IntegerField(primary_key=True, serialize=False)),
                ('describ', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat2',
            fields=[
                ('typeId', models.IntegerField(primary_key=True, serialize=False)),
                ('describ', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat3',
            fields=[
                ('typeId', models.IntegerField(primary_key=True, serialize=False)),
                ('describ', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('typeId', models.IntegerField(primary_key=True, serialize=False)),
                ('describ', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=15, unique=True)),
                ('userPw', models.CharField(max_length=200)),
                ('introduce', models.CharField(default='자기소개', max_length=50)),
                ('linkId', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
    ]
