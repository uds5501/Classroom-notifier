# Generated by Django 2.2.13 on 2020-06-29 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20181112_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('content', models.TextField()),
                ('class_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.Class')),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Teacher')),
            ],
            options={
                'verbose_name_plural': 'notifications',
            },
        ),
    ]
