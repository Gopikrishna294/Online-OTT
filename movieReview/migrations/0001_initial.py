# Generated by Django 3.2.9 on 2022-01-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('food_Id', models.AutoField(primary_key=True, serialize=False)),
                ('food_Name', models.CharField(max_length=50)),
                ('food_Price', models.FloatField()),
            ],
        ),
    ]
