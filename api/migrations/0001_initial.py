# Generated by Django 3.1 on 2020-08-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('m_title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('awards', models.IntegerField()),
            ],
        ),
    ]
