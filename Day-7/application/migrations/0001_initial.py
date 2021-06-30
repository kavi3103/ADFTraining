# Generated by Django 3.2.4 on 2021-06-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=200)),
                ('current_city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('qualification', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('pan', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=200)),
                ('request_id', models.IntegerField()),
            ],
        ),
    ]