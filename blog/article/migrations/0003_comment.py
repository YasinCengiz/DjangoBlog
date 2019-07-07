# Generated by Django 2.2.2 on 2019-07-07 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190705_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='name')),
                ('comment_content', models.CharField(max_length=256, verbose_name='comment')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Comment Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Article')),
            ],
        ),
    ]