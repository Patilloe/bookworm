# Generated by Django 5.0.6 on 2024-06-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_review_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
