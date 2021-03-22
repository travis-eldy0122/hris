# Generated by Django 2.1.7 on 2021-03-17 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtName', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PositionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionType', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(default='', max_length=255)),
                ('districtName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='RawData.District')),
            ],
        ),
        migrations.CreateModel(
            name='StaffData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surName', models.CharField(default='', max_length=500)),
                ('firstName', models.CharField(default='', max_length=500)),
                ('middleName', models.CharField(default='', max_length=500)),
                ('extensionName', models.CharField(default='', max_length=500)),
                ('dateBirth', models.DateField(null=True)),
                ('placeBirth', models.CharField(default='', max_length=500)),
                ('sex', models.CharField(default='', max_length=500)),
                ('civilStatus', models.CharField(default='', max_length=500)),
                ('gsisId', models.CharField(default='', max_length=500)),
                ('pagibigId', models.CharField(default='', max_length=500)),
                ('philhealthId', models.CharField(default='', max_length=500)),
                ('tinId', models.CharField(default='', max_length=500)),
                ('mobileNum', models.CharField(default='', max_length=500)),
                ('depedEmail', models.CharField(default='', max_length=500)),
                ('districtName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='RawData.District')),
                ('positionName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='RawData.Position')),
                ('schoolName', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='RawData.School')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='positionType',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='RawData.PositionType'),
        ),
    ]