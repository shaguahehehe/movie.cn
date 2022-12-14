# Generated by Django 2.2.28 on 2022-06-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_detail', '0003_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.FloatField()),
                ('movie_id', models.FloatField()),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'user_evaluation',
                'managed': False,
            },
        ),
    ]
