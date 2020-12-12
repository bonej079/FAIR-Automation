# Generated by Django 3.0.3 on 2020-12-08 18:23
from django.db import migrations, models
import requests
import json

def getBitlyLink(link):
    headers = {
        'Authorization': 'Bearer b182461614aa63cf46f8d154546767416ad8d747',
        'Content-Type': 'application/json',
    }
    data = '{ "long_url": "' + link + '", "domain": "bit.ly" }'
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
    response_dict = json.loads(response.text)
    return response_dict["link"]


def shortenLinks(apps, schema_editor):
    reusability = apps.get_model("portal", "reusability")
    findability = apps.get_model("portal", "findability")

    for obj in reusability.objects.all():
        if not obj.repositoryLink.startswith('No'):
            obj.shortRepoLink = getBitlyLink(obj.repositoryLink)
        else:
            obj.shortRepoLink = ""
        obj.save()

    for obj in findability.objects.all():
        if not obj.doiLink.startswith('No'):
            obj.shortDoiLink = getBitlyLink(obj.doiLink)
        else:
            obj.shortDoiLink = ""

        if not obj.downlink.startswith('No'):
            obj.shortDownLink = getBitlyLink(obj.downlink)
        else:
            obj.shortDownLink = ""
        obj.save()



class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20190509_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='findability',
            name='shortDoiLink',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='findability',
            name='shortDownLink',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='reusability',
            name='shortRepoLink',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.RunPython(shortenLinks)
    ]

