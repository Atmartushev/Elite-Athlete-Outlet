# Generated by Django 5.0.3 on 2024-05-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_productvariation_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('qualifications', models.TextField()),
            ],
        ),
    ]
