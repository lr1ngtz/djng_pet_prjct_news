# Generated by Django 3.2 on 2021-06-10 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_app.rubric')),
            ],
        ),
    ]
