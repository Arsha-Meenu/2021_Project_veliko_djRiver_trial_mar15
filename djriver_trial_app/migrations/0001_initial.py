# Generated by Django 3.1.7 on 2021-03-16 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('river', '0002_auto_20210316_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionYearMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_year', models.CharField(max_length=20)),
                ('academic_year', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.state')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheme_master_admission_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
