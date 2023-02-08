from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('pressure', models.FloatField()),
                ('humidity', models.FloatField()),
                ('timeData', models.DateTimeField()),
            ],
        ),
    ]
