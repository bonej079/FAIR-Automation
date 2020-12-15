from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Tool(models.Model):
    tool_name = models.CharField(max_length=200)
    isPrivate = models.BooleanField(default=False)
    owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    privateDesc = models.TextField(null=True)
    def __str__(self):
        return self.tool_name

class Findability(models.Model):
    tool = models.ForeignKey(Tool, on_delete = models.CASCADE)
    free_down = models.FloatField()
    downlink = models.TextField()
    doi = models.FloatField()
    doiLink = models.CharField(max_length=200)
    description = models.FloatField()
    descText = models.TextField()
    versions = models.FloatField()

class Accessibility(models.Model):
    tool = models.ForeignKey(Tool, on_delete = models.CASCADE)
    api = models.FloatField()
    commandLine = models.FloatField()

class Interoperability(models.Model):
    tool = models.ForeignKey(Tool, on_delete = models.CASCADE)
    compatibility = models.FloatField()
    winComp = models.BooleanField()
    macComp = models.BooleanField()
    unixComp = models.BooleanField()
    sourceCode = models.FloatField()

class Reusability(models.Model):
    tool = models.ForeignKey(Tool, on_delete = models.CASCADE)    
    public_repo = models.FloatField()
    repositoryLink = models.CharField(max_length=200)
    ontology = models.FloatField()
    ontUsed = models.CharField(max_length=200)
    documentation = models.FloatField()
    contact = models.FloatField()
    citation = models.FloatField()
    usesOnt = models.BooleanField(default=True)

class FairScore(models.Model):
    tool = models.ForeignKey(Tool, on_delete = models.CASCADE)
    findability = models.FloatField()
    accessibility = models.FloatField()
    interoperability = models.FloatField()
    reusability = models.FloatField()

class Pipeline(models.Model):
    owner = models.ForeignKey(get_user_model(), null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    findability = models.FloatField(null=True)
    accessibility = models.FloatField(null=True)
    interoperability = models.FloatField(null=True)
    reusability = models.FloatField(null=True)

class PipelineTools(models.Model):
    pipeline = models.ForeignKey(Pipeline, on_delete = models.CASCADE)
    tool = models.ForeignKey(Tool, related_name="tool", on_delete = models.CASCADE)
    toolBefore = models.ForeignKey(Tool, related_name="tool_before", on_delete = models.CASCADE, null=True)
    toolAfter = models.ForeignKey(Tool, related_name="tool_after", on_delete = models.CASCADE, null=True)
    position = models.IntegerField(null=True)
    branch = models.IntegerField(default=0)

class Publication(models.Model):
    name = models.CharField(max_length = 400)
    authors = models.CharField(max_length = 400) #Should we create an Author class ?
    link = models.CharField(max_length = 400)
