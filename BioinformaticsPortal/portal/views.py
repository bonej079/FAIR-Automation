from django.shortcuts import render, redirect
from portal.models import FairScore, Tool, Findability, Accessibility, Interoperability, Reusability, Pipeline, PipelineTools
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'portal/index.html', {
        'view_name': 'Home'
    })

def tools(request):
    if request.method == "POST":
        pipeline_id = list(request.POST.keys())[2]
        tool_id = request.POST['tool_id']
        pipelineTool = PipelineTools.objects.create(pipeline_id = pipeline_id, tool_id = tool_id) 

        pipeline_tools = PipelineTools.objects.select_related('tool').filter(pipeline_id = pipeline_id)
        f = 0
        a = 0
        i = 0
        r = 0
        for tool in pipeline_tools:
            fairscore = FairScore.objects.get(tool_id = tool.tool_id)
            f = f + fairscore.findability
            a = a + fairscore.accessibility
            i = i + fairscore.interoperability
            r = r + fairscore.reusability
        
        f = round(f / len(pipeline_tools), 2)
        a = round(a / len(pipeline_tools), 2)
        i = round(i / len(pipeline_tools), 2)
        r = round(r / len(pipeline_tools), 2)
        pipeline = Pipeline.objects.get(id=pipeline_id)
        pipeline.findability = f
        pipeline.accessibility = a
        pipeline.interoperability = i
        pipeline.reusability = r
        pipeline.save()

    tools = FairScore.objects.select_related('tool').filter(tool__isPrivate=False)
    
    if request.user.is_authenticated:
        private = Tool.objects.filter(isPrivate=True, owner_id=request.user.id).all()
        context = {
            'view_name': 'Tools',
            'tools': tools,
            'private': private
        }
    else:
        context = {
            'view_name': 'Tools',
            'tools': tools
        }

    return render(request, 'portal/tools.html', context)

def details(request, id):

    if request.POST:
        print(request.POST)
        if request.POST['scope'] == 'findability':
            upFind = Findability.objects.get(tool_id=id)
            updateFair = FairScore.objects.get(tool_id=id)
            score = 0

            if request.POST['downLink'] != upFind.downlink:
                upFind.downlink = request.POST['downLink']
                if request.POST['downLink'] == "":
                    upFind.free_down = 0
                else:
                    upFind.free_down = 8
                    score = score + 8
            else:
                score = score + upFind.free_down

            if request.POST['doiLink'] != upFind.doiLink:
                upFind.doiLink = request.POST['doiLink']
                if request.POST['doiLink'] == "":
                    upFind.doi = 0
                else:
                    upFind.doi = 5
                    score = score + 5
            else:
                score = score + upFind.doi

            if request.POST['description'] != upFind.descText:
                upFind.descText = request.POST['description']
                if request.POST['description'] == "":
                    upFind.description = 0
                else:
                    upFind.description = 5
                    score = score + 5
            else:
                score = score + upFind.description

            if request.POST['version'] != upFind.versions:
                score = score + float(request.POST['version'])
                upFind.versions = request.POST['version']
            else:
                score = score + upFind.version

            updateFair.findability = score * 5
            updateFair.save()
            upFind.save()

        if request.POST['scope'] == 'accessibility':
            upAcc = Accessibility.objects.get(tool_id=id)
            updateFair = FairScore.objects.get(tool_id=id)
            score = 0
            if request.POST['api'] != upAcc.api:
                upAcc.api = request.POST['api']
                score = score + float(request.POST['api'])
            updateFair.accessibility = score * 20
            updateFair.save()
            upAcc.save()

        if request.POST['scope'] == 'interoperability':
            upInt = Interoperability.objects.get(tool_id=id)
            

    tool = Tool.objects.get(id=id)
    findability = Findability.objects.get(tool_id=id)
    accessibility = Accessibility.objects.get(tool_id=id)
    interoperability = Interoperability.objects.get(tool_id=id)
    reusability = Reusability.objects.get(tool_id=id)
    fair = FairScore.objects.get(tool_id=id)
    
    context = {
        'view_name': 'Details',
        'tool': tool,
        'findability': findability,
        'accessibility': accessibility,
        'interoperability': interoperability,
        'reusability': reusability,
        'fair': fair
    }
    return render(request, 'portal/tools/details.html', context)

def add(request, id):
    pipelines = Pipeline.objects.filter(owner_id = request.user.id)
    tool = Tool.objects.get(id=id)

    context = {
        'view_name': 'Add to pipeline',
        'pipelines': pipelines,
        'tool': tool,
    }
    return render(request, 'portal/tools/add.html', context)

@login_required(login_url='/accounts/login/')
def pipelines(request):
    pipelines = Pipeline.objects.filter(owner_id = request.user.id)
    if request.POST:
        print("post request")
        tool_id = list(request.POST.keys())[2]
        pipeline_id = request.POST['pipeline_id']
        pipelineTool = PipelineTools.objects.get(pipeline_id=pipeline_id, tool_id=tool_id).delete() 

        pipeline_tools = PipelineTools.objects.select_related('tool').filter(pipeline_id = pipeline_id)
        f = 0
        a = 0
        i = 0
        r = 0
        for tool in pipeline_tools:
            fairscore = FairScore.objects.get(tool_id = tool.tool_id)
            f = f + fairscore.findability
            a = a + fairscore.accessibility
            i = i + fairscore.interoperability
            r = r + fairscore.reusability
        
        f = round(f / len(pipeline_tools), 2)
        a = round(a / len(pipeline_tools), 2)
        i = round(i / len(pipeline_tools), 2)
        r = round(r / len(pipeline_tools), 2)
        pipeline = Pipeline.objects.get(id=pipeline_id)
        pipeline.findability = f
        pipeline.accessibility = a
        pipeline.interoperability = i
        pipeline.reusability = r
        pipeline.save()


    context = {
        'view_name': 'Pipelines',
        'pipelines': pipelines
    }
    return render(request, 'portal/pipelines.html', context)

@login_required(login_url='/accounts/login/')
def pipelineDetails(request, id):
    tools = PipelineTools.objects.select_related('tool', 'pipeline').filter(pipeline_id = id).order_by('position')
    if request.user.id is not tools[0].pipeline.owner_id:
        return redirect('pipelines')
    
    context = {
        'view_name': 'Pipeline Details',
        'tools': tools
    }
    return render(request, 'portal/pipelines/details.html', context)

def createPipeline(request):
    if request.POST:
        pipeline_name=request.POST['name']
        pipeline = Pipeline.objects.create(name=pipeline_name, owner_id=request.user.id)

        context={
            'view_name': 'success',
            'name': pipeline_name
        }
        return render(request, 'portal/pipelines/success.html', context)
    return render(request, 'portal/pipelines/create.html')

@login_required(login_url='/accounts/login/')
def privateDetails(request, id):
    tool = Tool.objects.get(id=id)
    if request.user.id is not tool.owner_id:
        return redirect('tools')
    else:
        context={
            'view_name': 'Private Tool details',
            'tool': tool
        }
        return render(request, 'portal/tools/private.html', context)

def refineFindability(request, id):
    tool = FairScore.objects.select_related('tool').get(tool_id=id)
    findability = Findability.objects.get(tool_id=id)
    context = {
        'view_name': 'Refine findability',
        'tool': tool,
        'findability': findability
    }
    return render(request, 'portal/refine/findability.html', context)

def refineAccessibility(request, id):
    tool = FairScore.objects.select_related('tool').get(tool_id=id)
    accessibility = Accessibility.objects.get(tool_id=id)
    context = {
        'view_name': 'Refine accessibility',
        'tool': tool,
        'accessibility': accessibility
    }
    return render(request, 'portal/refine/accessibility.html', context)

def refineInteroperability(request, id):
    tool = FairScore.objects.select_related('tool').get(tool_id=id)
    interoperability = Interoperability.objects.get(tool_id=id)
    context = {
        'view_name': 'Refine interoperability',
        'tool': tool,
        'interoperability': interoperability
    }
    return render(request, 'portal/refine/interoperability.html', context)