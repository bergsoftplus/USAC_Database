# Generated by Django 2.0 on 2017-12-29 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('flyer_url', models.URLField(max_length=255, null=True)),
                ('flyer', models.FileField(blank=True, null=True, upload_to='uploads/flyers/')),
                ('website_url', models.URLField(max_length=255, null=True)),
                ('online_reg', models.URLField(max_length=255, null=True)),
                ('permit_number', models.CharField(max_length=255, unique=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='usac.Director')),
            ],
        ),
        migrations.CreateModel(
            name='EventDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_id', models.IntegerField(default=None, null=True)),
                ('day', models.DateField()),
                ('url', models.URLField(max_length=255)),
                ('multi_page', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usac.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LapTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laps', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('license', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Promoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('race_id', models.IntegerField()),
                ('url', models.URLField(max_length=255)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usac.Event')),
                ('event_day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usac.EventDay')),
            ],
        ),
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('points', models.CharField(blank=True, max_length=255, null=True)),
                ('city_state', models.CharField(blank=True, max_length=255, null=True)),
                ('result_time', models.CharField(blank=True, max_length=255, null=True)),
                ('usac', models.CharField(blank=True, max_length=255, null=True)),
                ('bib', models.CharField(blank=True, max_length=255, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usac.Participant')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usac.Race')),
            ],
        ),
        migrations.AddField(
            model_name='laptimes',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usac.RaceResult'),
        ),
        migrations.AddField(
            model_name='event',
            name='etypes',
            field=models.ManyToManyField(blank=True, default=list, to='usac.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='promoter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='usac.Promoter'),
        ),
    ]
