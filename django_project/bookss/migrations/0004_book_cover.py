# Generated by Django 4.0.3 on 2023-03-13 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookss', '0003_alter_review_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='cover/'),
        ),
    ]