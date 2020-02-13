# Generated by Django 3.0.3 on 2020-02-13 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20200213_1013'),
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Batch'),
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
