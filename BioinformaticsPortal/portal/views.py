from django.shortcuts import render, redirect
from portal.models import FairScore, Tool, Findability, Accessibility, Interoperability, Reusability, Pipeline, PipelineTools
from django.contrib.auth.decorators import login_required
import yaml
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.exceptions import ObjectDoesNotExist
from googleapiclient.discovery import build
from selenium import webdriver
from crossref.restful import Works, Journals
import requests
import json

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
                    upFind.shortDownLink = ""
                else:
                    upFind.free_down = 8
                    score = score + 8
                    upFind.shortDownLink = getBitlyLink(request.POST["downLink"])
            else:
                score = score + upFind.free_down

            if request.POST['doiLink'] != upFind.doiLink:
                upFind.doiLink = request.POST['doiLink']
                if request.POST['doiLink'] == "":
                    upFind.doi = 0
                    upFind.shortDoiLink = ""
                else:
                    upFind.doi = 5
                    score = score + 5
                    upFind.shortDoiLink = getBitlyLink(request.POST["doiLink"])
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
            else:
                score = score + upAcc.api
            if request.POST['cli'] != upAcc.commandLine:
                upAcc.commandLine = request.POST['cli']
                score = score + float(request.POST['cli'])
            else:
                score = score + upAcc.commandLine
            updateFair.accessibility = score * 10
            updateFair.save()
            upAcc.save()

        if request.POST['scope'] == 'interoperability':
            upInt = Interoperability.objects.get(tool_id=id)
            updateFair = FairScore.objects.get(tool_id=id)
            score = 0
            compScore = 0
            if request.POST['win'] != upInt.winComp:
                upInt.winComp = request.POST['win']
                compScore = compScore + float(request.POST['win'])
            else:
                compScore = compScore + upInt.winComp
            if request.POST['mac'] != upInt.macComp:
                upInt.macComp = request.POST['mac']
                compScore = compScore + float(request.POST['mac'])
            else:
                compScore = compScore + upInt.macComp
            if request.POST['unix'] != upInt.unixComp:
                upInt.unixComp = request.POST['unix']
                compScore = compScore + float(request.POST['unix'])
            else:
                compScore = compScore + upInt.unixComp
            if request.POST['sc'] != upInt.sourceCode:
                upInt.sourceCode = request.POST['sc']
                score = score + float(request.POST['sc'])
            else:
                score = score + upInt.sourceCode
            updateFair.interoperability = round(((compScore * (5/3)) * 10), 2) + (score*10)
            updateFair.save()
            upInt.save()

        if request.POST['scope'] == 'reusability':
            active_ontologies = []
            upRe = Reusability.objects.get(tool_id=id)
            updateFair = FairScore.objects.get(tool_id=id)
            score = 0
            if request.POST['ontologies'] == '0':
                upRe.usesOnt = 0
                upRe.ontUsed = ""
                if request.POST['pubRep'] != upRe.repositoryLink:
                    if request.POST['pubRep'] == "":
                        upRe.public_repo = 0
                        upRe.shortRepoLink = ""
                    else:
                        upRe.public_repo = 8
                        score = score + 8
                        upRe.shortRepoLink = getBitlyLink(request.POST["pubRep"])
                else:
                    score = score + upRe.public_repo
                if request.POST['documentation'] != upRe.documentation:
                    if request.POST['documentation'] == '0':
                        upRe.documentation = request.POST['documentation']
                    else:
                        upRe.documentation = int(request.POST['documentation']) + 2
                        score = score + float(request.POST['documentation']) + 2
                else:
                    if upRe.documentation != 0:
                        score = score + 6
                        upRe.documentation = 6
                if request.POST['contact'] != upRe.contact:
                    if request.POST['contact'] == '0':
                        upRe.contact = request.POST['contact']
                    else:
                        upRe.contact = int(request.POST['contact']) + 1
                        score = score + float(request.POST['contact']) + 1
                else:
                    if upRe.contact != 0:
                        score = score + 3
                        upRe.contact = 3
                if request.POST['citation'] != upRe.citation:
                    if request.POST['citation'] == '0':
                        upRe.citation = request.POST['citation']
                    else:
                        upRe.citation = int(request.POST['citation']) + 1
                        score = score + float(request.POST['citation']) + 1
                else:
                    if upRe.citation != 0:
                        score = score + 3
                        upRe.citation = 3
            else:
                upRe.usesOnt = 1
                if request.POST['ontUsed'] != "":
                    # ont = "C:/Users/Nigel/Desktop/FAIR-Automation/BioinformaticsPortal/portal/static/data/ontologies.yml"
                    ont = "/media/jbon4/Data/Development/python/Bioinformatics Portal/FAIR-Automation/BioinformaticsPortal/static/data/ontologies.yml"
                    with open(ont, 'r') as ont:
                        try:
                            content = yaml.load(ont)
                            for item in content.items():
                                x = item[1]
                                for i in range(len(x)):
                                    if x[i]["activity_status"] == "active":
                                        active_ontologies.append(x[i]["title"])
                        except yaml.YAMLError as exc:
                            print(exc)
                    for ont in active_ontologies:
                        if ont in request.POST['ontUsed']:
                            score = 4
                            upRe.ontology = 4
                    if score == 0:
                        score = 2
                        upRe.ontology = 2
                    upRe.ontUsed = request.POST['ontUsed']
                else:
                    upRe.ontUsed = ""
                    upRe.ontology = 0
                if request.POST['pubRep'] != upRe.repositoryLink:
                    if request.POST['pubRep'] == "":
                        upRe.public_repo = 0
                        upRe.shortRepoLink = ""
                    else:
                        upRe.public_repo = 8
                        score = score + 8
                        upRe.shortRepoLink = getBitlyLink(request.POST["pubRep"])
                else:
                    score = score + upRe.public_repo
                if request.POST['documentation'] != upRe.documentation:
                    if request.POST['documentation'] == '0':
                        upRe.documentation = request.POST['documentation']
                    else:
                        upRe.documentation = request.POST['documentation']
                        score = score + float(request.POST['documentation'])
                else:
                    score = score + upRe.documentation
                if request.POST['contact'] != upRe.contact:
                    if request.POST['contact'] == '0':
                        upRe.contact = request.POST['contact']
                    else:
                        upRe.contact = request.POST['contact']
                        score = score + float(request.POST['contact'])
                else:
                    score = score + upRe.contact
                if request.POST['citation'] != upRe.citation:
                    if request.POST['citation'] == '0':
                        upRe.citation = request.POST['citation']
                    else:
                        upRe.citation = request.POST['citation']
                        score = score + float(request.POST['citation'])
                else:
                    score = score + upRe.citation 

            updateFair.reusability = score * 5
            updateFair.save()
            upRe.save() 


            

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
    
    if request.POST:
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

    pipelines = Pipeline.objects.filter(owner_id = request.user.id)
    context = {
        'view_name': 'Pipelines',
        'pipelines': pipelines
    }
    return render(request, 'portal/pipelines.html', context)

@login_required(login_url='/accounts/login/')
def pipelineDetails(request, id):
    pipeline = Pipeline.objects.get(id=id)
    tools = PipelineTools.objects.select_related('tool', 'pipeline').filter(pipeline_id = id).order_by('position')
    toolScores = []
    for tool in tools:
        t = FairScore.objects.select_related('tool').get(tool_id=tool.tool_id)
        toolScores.append(t)
    if request.user.id is not pipeline.owner_id:
        return redirect('pipelines')
    
    context = {
        'view_name': 'Pipeline Details',
        'tools': tools,
        'scores': toolScores,
        'pipeline': pipeline
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

def refineReusability(request, id):
    tool = FairScore.objects.select_related('tool').get(tool_id=id)
    reusability = Reusability.objects.get(tool_id=id)
    context = {
        'view_name': 'Refine reusability',
        'tool': tool,
        'reusability': reusability
    }
    return render(request, 'portal/refine/reusability.html', context)

def getBitlyLink(link):
    headers = {
        'Authorization': 'Bearer b182461614aa63cf46f8d154546767416ad8d747',
        'Content-Type': 'application/json',
    }
    data = '{ "long_url": "' + link + '", "domain": "bit.ly" }'
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
    response_dict = json.loads(response.text)
    return response_dict["link"]


def addTool(request):
    if request.POST:
        print(request.POST)
        if request.POST['website']:
            tool=""
            try:
                tool = Tool.objects.get(tool_name=request.POST['name'])
            except ObjectDoesNotExist:
                tool = ""
            if not tool:
                active_ontologies = []
                # with open("C:/Users/Nigel/Desktop/FAIR-Automation/BioinformaticsPortal/portal/static/data/ontologies.yml", 'r') as ont:
                with open("/media/jbon4/Data/Development/python/Bioinformatics Portal/FAIR-Automation/BioinformaticsPortal/static/data/ontologies.yml", 'r') as ont:
                    try:
                        content = yaml.load(ont)
                        for item in content.items():
                            x = item[1]
                            for i in range(len(x)):
                                if x[i]["activity_status"] == "active":
                                    active_ontologies.append(x[i]["title"].lower())
                    except yaml.YAMLError as exc:
                        print(exc)

                search_phrase = request.POST['name']

                driver = webdriver.Firefox()
                link = request.POST['website']
                download = ""
                publicRepo = ""
                documentation = ""
                versElem = ""
                windowsComp = ""
                unixComp = ""
                macComp = ""
                about = ""
                citeInfo = ""
                contact = ""
                apiInfo = ""
                doi = ""
                doiTitle=""
                ontology=""
                ontologies=""
                source = ""
                cli = ""
                git= ""

                if link:
                    driver.get(link)
                    try:
                        elem = driver.find_element_by_partial_link_text("Download")
                        download = elem.get_attribute('innerHTML')
                        elem.click()  
                    except Exception:
                        pass

                    if "github.com" in driver.current_url:
                        # print("public resource available")
                        publicRepo = driver.current_url
                        documentation = "available"
                        download = driver.current_url
                        versElem = "available"
                        source = "available"
                    else:
                        try:
                            git = driver.find_element_by_partial_link_text("github.com")
                            print(git)
                        except Exception:
                            pass
                        if not git:
                            try:
                                git = driver.find_element_by_xpath("//*[contains(text(), 'GitHub')]")
                            except Exception:
                                pass
                        if git:
                            # print("public resource available")
                            publicRepo = git
                            documentation = "available"
                            download=git
                            versElem = "available"
                            source = "available"
                    if not versElem:
                        try:    
                            versElem = driver.find_element_by_xpath("//*[contains(text(), 'Older versions')]")
                        except Exception:
                            pass
                            
                        if not versElem:
                            try:
                                versElem = driver.find_element_by_xpath("//*[contains(text(), 'Previous versions')]")
                            except Exception:
                                pass
                    try:
                        documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                    except Exception:
                        pass

                    if not documentation:
                        try:
                            documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'source code')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source code')]")
                        except Exception:
                            pass
                    
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source Code')]")
                        except Exception:
                            pass

                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'command line')]")
                        except Exception:
                            pass

                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command line')]")
                        except Exception:
                            pass

                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command Line')]")
                        except Exception:
                            pass

                    try:
                        windowsComp = driver.find_element_by_xpath("//*[contains(text(), 'Windows')]")
                    except Exception:
                        pass

                    try:
                        unixComp = driver.find_element_by_xpath("//*[contains(text(), 'UNIX')]")
                    except Exception:
                        pass
                    
                    if not unixComp:
                        try:
                            driver.find_element_by_xpath("//*[contains(text(), 'Unix')]")
                        except Exception:
                            pass

                    try:        
                        macComp = driver.find_element_by_xpath("//*[contains(text(), 'Mac')]")
                    except Exception:
                        pass

                    driver.get(link)
                    if not publicRepo:
                        if "github.com" in driver.current_url:
                            # print("public resource available")
                            publicRepo = driver.current_url
                            documentation = "available"
                            download = driver.current_url
                            versElem = "available"
                            source = "available"
                        else:
                            try:
                                git = driver.find_element_by_partial_link_text("github.com")
                                print(git)
                            except Exception:
                                pass
                            if not git:
                                try:
                                    git = driver.find_element_by_xpath("//*[contains(text(), 'GitHub')]")
                                except Exception:
                                    pass
                            if git:
                                # print("public resource available")
                                publicRepo = git
                                documentation = "available"
                                download=git
                                versElem = "available"
                                source = "available"
                    if not versElem:
                        try:    
                            versElem = driver.find_element_by_xpath("//*[contains(text(), 'Older versions')]")
                        except Exception:
                            pass
                            
                        if not versElem:
                            try:
                                versElem = driver.find_element_by_xpath("//*[contains(text(), 'Previous versions')]")
                            except Exception:
                                pass
                    if not documentation:
                        try:
                            documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                        except Exception:
                            pass
                    if not documentation:
                        try:
                            documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'source code')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source code')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source Code')]")
                        except Exception:
                            pass
                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'command line')]")
                        except Exception:
                            pass
                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command line')]")
                        except Exception:
                            pass
                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command Line')]")
                        except Exception:
                            pass
                    if not windowsComp:
                        try:
                            windowsComp = driver.find_element_by_xpath("//*[contains(text(), 'Windows')]")
                        except Exception:
                            pass
                    if not unixComp:
                        try:
                            unixComp = driver.find_element_by_xpath("//*[contains(text(), 'UNIX')]")
                        except Exception:
                            pass
                    if not unixComp:
                        try:
                            driver.find_element_by_xpath("//*[contains(text(), 'Unix')]")
                        except Exception:
                            pass 
                    if not macComp:
                        try:        
                            macComp = driver.find_element_by_xpath("//*[contains(text(), 'Mac')]")
                        except Exception:
                            pass
                    try:
                        about = driver.find_element_by_partial_link_text("About")
                    except Exception:
                        pass
                    
                    if not about:
                        try:
                            about = driver.find_element_by_xpath("//*[contains(text(), 'Introduction')]")
                        except Exception:
                            pass

                        if not about:
                            try:
                                about = driver.find_element_by_xpath("//*[contains(text(), 'About')]")
                            except Exception:
                                pass

                            if not about:
                                try:
                                    about = driver.find_element_by_xpath("//*[contains(text(), 'Description')]")
                                except Exception:
                                    pass
                                
                                if not about:
                                    try:
                                        about = driver.find_element_by_xpath("//*[contains(text(), 'desc')]")
                                    except Exception:
                                        pass
                    try:
                        citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Citing')]")
                    except Exception:
                        pass
                    if not citeInfo:
                        try:
                            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'References')]")
                        except Exception:
                            pass
                    if not citeInfo:
                        try:
                            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Citations')]")
                        except Exception:
                            pass
                    try:
                        contact = driver.find_element_by_partial_link_text("Contact")
                    except Exception:
                        pass
                    if not contact:
                        try:
                            contact = driver.find_element_by_xpath("//*[contains(text(), 'email')]")
                        except Exception:
                            pass
                    if not contact:
                        try:
                            contact = driver.find_element_by_xpath("//*[contains(text(), 'Contact')]")
                        except Exception:
                            pass
                    if not contact:
                        try:
                            contact = driver.find_element_by_xpath("//*[contains(text(), 'contact')]")
                        except Exception:
                            pass
                    try:            
                        apiInfo = driver.find_element_by_partial_link_text("API")
                    except Exception:
                        pass
                    if not apiInfo:
                        try:
                            apiInfo = driver.find_element_by_xpath("//*[contains(text(), 'API')]")
                        except Exception:
                            pass
                    try:
                        for ont in active_ontologies:
                            if ont in driver.page_source.lower():
                                ontology="available"
                                ontologies = ontologies + ont
                    except Exception:
                        pass
                    try:
                        doi = driver.find_element_by_xpath("//*[contains(text(), 'doi')]")
                        doi.click()
                        print(driver.current_url)
                        doi = driver.find_element_by_class_name('epub-doi')
                    except Exception:
                        pass
                    if not doi:
                        try:
                            doi = driver.find_element_by_xpath("//*[contains(text(), 'doi')]")
                            doi.click()
                            print(driver.current_url)
                            doiTitle = driver.find_element_by_tag_name("title").get_attribute("textContent")
                            doi = ""
                        except Exception:
                            pass
                if not doi:
                    works = Works()
                    i=0
                    if doiTitle:
                        w1 = works.query(title=doiTitle).filter(type="journal-article").sort('relevance')
                        for item in w1:
                            i=i+1
                            if item['title'] is doiTitle:
                                doi = item['DOI']
                                break
                            if i > 10:
                                break
                    else:
                        w1 = works.query(title=search_phrase).filter(type="journal-article").sort("relevance")
                        for item in w1:
                            i=i+1
                            if search_phrase in item['title']:
                                doi = item['DOI']
                                break
                            if i > 10:
                                break
                if download:
                    downloadVal = 8.0
                else:
                    downloadVal = 0.0
                if publicRepo:
                    publicRepoVal = 8.0
                else:
                    publicRepoVal = 0.0
                if documentation:
                    documentationVal = 4.0
                else:
                    documentationVal = 0.0
                if versElem:
                    versVal = 2.0
                else:
                    versVal = 0.0
                compVal = 0.0
                if not windowsComp and not unixComp and not macComp:
                    compVal=0.0
                    winComp=0
                    unixComp=0
                    macComp=0
                else:
                    if windowsComp:
                        compVal = compVal + (5/3)
                        winComp=1.0
                    else:
                        winComp = 0.0
                    if unixComp:
                        compVal = compVal + (5/3)
                        unixComp=1.0
                    else:
                        unixComp=0.0
                    if macComp:
                        compVal = compVal + (5/3)
                        macComp=1.0
                    else:
                        macComp=0.0
                if about:
                    aboutVal = 5.0
                else:
                    aboutVal = 0.0
                if citeInfo:
                    citeVal = 2.0
                else:
                    citeVal = 0.0
                if contact:
                    contactVal = 2.0
                else:
                    contactVal = 0.0
                if apiInfo:
                    apiVal = 5.0
                else:
                    apiVal = 0.0
                if doi:
                    doiVal = 5.0
                else:
                    doiVal = 0.0
                if ontology:
                    ontologyVal = 4.0
                else:
                    ontologyVal = 0.0
                if source:
                    sourceVal = 5.0
                else:
                    sourceVal = 0.0
                if cli:
                    cliVal = 5.0
                else:
                    cliVal=0.0

                findability = ((downloadVal + doiVal + aboutVal + versVal) / (8+5+5+2)) * 100
                findability = round(findability, 2)
                accessiblity = ((apiVal+cliVal)/(5+5))*100
                accessiblity = round(accessiblity, 2)
                interoperability = ((compVal+sourceVal)/(5+5)) * 100
                interoperability = round(interoperability, 2)
                reusability = ((publicRepoVal + ontologyVal + documentationVal + contactVal + citeVal) / (8+4+4+2+2)) * 100

                doiShort = ""
                downloadShort =""
                publicRepoShort = ""
                if doi:
                    doiShort = getBitlyLink(doi)
                if download:
                    downloadShort = getBitlyLink(download)
                if publicRepo:
                    publicRepoShort = getBitlyLink(publicRepo)

                tool = Tool.objects.create(tool_name=request.POST['name'], isPrivate=0)
                tool = Tool.objects.get(tool_name = request.POST['name'])
                fairScore = FairScore.objects.create(findability=findability, accessibility = accessiblity, interoperability = interoperability, reusability = reusability, tool_id = tool.id)
                find = Findability.objects.create(free_down=downloadVal, doi=doiVal, description = aboutVal, versions = versVal, tool_id=tool.id, doiLink=doi, downlink=download, shortDoiLink=doiShort, shortDownLink=downloadShort)
                acc = Accessibility.objects.create(api=apiVal, tool_id=tool.id, commandLine=cliVal)
                interop = Interoperability.objects.create(compatibility=compVal, tool_id=tool.id, macComp=macComp, unixComp=unixComp, winComp=winComp, sourceCode=sourceVal)
                reuse= Reusability.objects.create(public_repo=publicRepoVal, ontology=ontologyVal, documentation=documentationVal, contact=contactVal, citation=citeVal, tool_id=tool.id, repositoryLink=publicRepo, ontUsed=ontologies, usesOnt=1, shortRepoLink=publicRepoShort)
        else:
            tool=""
            try:
                tool = Tool.objects.get(tool_name=request.POST['name'])
            except ObjectDoesNotExist:
                tool = ""
            if not tool:
                active_ontologies = []
                # with open("C:/Users/Nigel/Desktop/FAIR-Automation/BioinformaticsPortal/portal/static/data/ontologies.yml", 'r') as ont:
                with open("/media/jbon4/Data/Development/python/Bioinformatics Portal/FAIR-Automation/BioinformaticsPortal/static/data/ontologies.yml", 'r') as ont:
                    try:
                        content = yaml.load(ont)
                        for item in content.items():
                            x = item[1]
                            for i in range(len(x)):
                                if x[i]["activity_status"] == "active":
                                    active_ontologies.append(x[i]["title"].lower())
                    except yaml.YAMLError as exc:
                        print(exc)
                my_api_key = "AIzaSyAqqbU_8-csEQuknlFfEfccDnviAXSpH9o"
                my_cse_id = "010537144392431308903:g2eqgue84js"
                search_phrase = request.POST['name']
                driver = webdriver.Firefox()
                def google_search(search_term, api_key, cse_id, **kwargs):
                    service = build("customsearch", "v1", developerKey=api_key)
                    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
                    return res['items']
                def findPage(results, search_phrase):
                    phrases = ["protein", "dna", "bioinformatics", "genome", "nucleotide", "biological", "biotechnology", "alignment", "amino acid", "autoradiography", "autosomal", "blotting", "blots", "cell", "computational biology", "sequencing", "similarity", "cluster", "cytoplasm", "enzyme", "gene", "genomics", "immunoglobuline", "lead", "mitosis"]
                    for result in results:
                        if search_phrase in result["title"].lower():
                            driver.get(result["link"])
                            for phrase in phrases:
                                if phrase in driver.page_source.lower():
                                    link=result["link"]
                                    return link
                results = google_search(search_phrase ,my_api_key, my_cse_id, num=20)
                link = findPage(results, search_phrase)
                download = ""
                publicRepo = ""
                documentation = ""
                versElem = ""
                windowsComp = ""
                unixComp = ""
                macComp = ""
                about = ""
                citeInfo = ""
                contact = ""
                apiInfo = ""
                doi = ""
                doiTitle=""
                ontology=""
                ontologies=""
                source = ""
                cli = ""
                git= ""
                if link:
                    driver.get(link)
                    try:
                        elem = driver.find_element_by_partial_link_text("Download")
                        download = elem.get_attribute('innerHTML')
                        elem.click()  
                    except Exception:
                        pass
                    if "github.com" in driver.current_url:
                        # print("public resource available")
                        publicRepo = driver.current_url
                        documentation = "available"
                        download = driver.current_url
                        versElem = "available"
                        source = "available"
                    else:
                        try:
                            git = driver.find_element_by_partial_link_text("github.com")
                            print(git)
                        except Exception:
                            pass
                        if not git:
                            try:
                                git = driver.find_element_by_xpath("//*[contains(text(), 'GitHub')]")
                            except Exception:
                                pass
                        if git:
                            # print("public resource available")
                            publicRepo = git
                            documentation = "available"
                            download=git
                            versElem = "available"
                            source = "available"
                    if not versElem:
                        try:    
                            versElem = driver.find_element_by_xpath("//*[contains(text(), 'Older versions')]")
                        except Exception:
                            pass
                            
                        if not versElem:
                            try:
                                versElem = driver.find_element_by_xpath("//*[contains(text(), 'Previous versions')]")
                            except Exception:
                                pass
                    try:
                        documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                    except Exception:
                        pass

                    if not documentation:
                        try:
                            documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'source code')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source code')]")
                        except Exception:
                            pass
                    
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source Code')]")
                        except Exception:
                            pass

                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'command line')]")
                        except Exception:
                            pass

                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command line')]")
                        except Exception:
                            pass

                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command Line')]")
                        except Exception:
                            pass

                    try:
                        windowsComp = driver.find_element_by_xpath("//*[contains(text(), 'Windows')]")
                    except Exception:
                        pass

                    try:
                        unixComp = driver.find_element_by_xpath("//*[contains(text(), 'UNIX')]")
                    except Exception:
                        pass
                    
                    if not unixComp:
                        try:
                            driver.find_element_by_xpath("//*[contains(text(), 'Unix')]")
                        except Exception:
                            pass

                    try:        
                        macComp = driver.find_element_by_xpath("//*[contains(text(), 'Mac')]")
                    except Exception:
                        pass

                    driver.get(link)
                    if not publicRepo:
                        if "github.com" in driver.current_url:
                            # print("public resource available")
                            publicRepo = driver.current_url
                            documentation = "available"
                            download = driver.current_url
                            versElem = "available"
                            source = "available"
                        else:
                            try:
                                git = driver.find_element_by_partial_link_text("github.com")
                                print(git)
                            except Exception:
                                pass
                            if not git:
                                try:
                                    git = driver.find_element_by_xpath("//*[contains(text(), 'GitHub')]")
                                except Exception:
                                    pass
                            if git:
                                # print("public resource available")
                                publicRepo = git
                                documentation = "available"
                                download=git
                                versElem = "available"
                                source = "available"
                    if not versElem:
                        try:    
                            versElem = driver.find_element_by_xpath("//*[contains(text(), 'Older versions')]")
                        except Exception:
                            pass
                            
                        if not versElem:
                            try:
                                versElem = driver.find_element_by_xpath("//*[contains(text(), 'Previous versions')]")
                            except Exception:
                                pass
                    if not documentation:
                        try:
                            documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                        except Exception:
                            pass
                    if not documentation:
                        try:
                            documentation = driver.find_element_by_xpath("//*[contains(text(), 'Documentation')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'source code')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source code')]")
                        except Exception:
                            pass
                    if not source:
                        try:
                            source = driver.find_element_by_xpath("//*[contains(text(), 'Source Code')]")
                        except Exception:
                            pass
                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'command line')]")
                        except Exception:
                            pass
                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command line')]")
                        except Exception:
                            pass
                    if not cli:
                        try:
                            cli = driver.find_element_by_xpath("//*[contains(text(), 'Command Line')]")
                        except Exception:
                            pass
                    if not windowsComp:
                        try:
                            windowsComp = driver.find_element_by_xpath("//*[contains(text(), 'Windows')]")
                        except Exception:
                            pass
                    if not unixComp:
                        try:
                            unixComp = driver.find_element_by_xpath("//*[contains(text(), 'UNIX')]")
                        except Exception:
                            pass
                    if not unixComp:
                        try:
                            driver.find_element_by_xpath("//*[contains(text(), 'Unix')]")
                        except Exception:
                            pass 
                    if not macComp:
                        try:        
                            macComp = driver.find_element_by_xpath("//*[contains(text(), 'Mac')]")
                        except Exception:
                            pass
                    try:
                        about = driver.find_element_by_partial_link_text("About")
                    except Exception:
                        pass
                    
                    if not about:
                        try:
                            about = driver.find_element_by_xpath("//*[contains(text(), 'Introduction')]")
                        except Exception:
                            pass

                        if not about:
                            try:
                                about = driver.find_element_by_xpath("//*[contains(text(), 'About')]")
                            except Exception:
                                pass

                            if not about:
                                try:
                                    about = driver.find_element_by_xpath("//*[contains(text(), 'Description')]")
                                except Exception:
                                    pass
                                
                                if not about:
                                    try:
                                        about = driver.find_element_by_xpath("//*[contains(text(), 'desc')]")
                                    except Exception:
                                        pass
                    try:
                        citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Citing')]")
                    except Exception:
                        pass
                    if not citeInfo:
                        try:
                            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'References')]")
                        except Exception:
                            pass
                    if not citeInfo:
                        try:
                            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Citations')]")
                        except Exception:
                            pass
                    try:
                        contact = driver.find_element_by_partial_link_text("Contact")
                    except Exception:
                        pass
                    if not contact:
                        try:
                            contact = driver.find_element_by_xpath("//*[contains(text(), 'email')]")
                        except Exception:
                            pass
                    if not contact:
                        try:
                            contact = driver.find_element_by_xpath("//*[contains(text(), 'Contact')]")
                        except Exception:
                            pass
                    if not contact:
                        try:
                            contact = driver.find_element_by_xpath("//*[contains(text(), 'contact')]")
                        except Exception:
                            pass
                    try:            
                        apiInfo = driver.find_element_by_partial_link_text("API")
                    except Exception:
                        pass
                    if not apiInfo:
                        try:
                            apiInfo = driver.find_element_by_xpath("//*[contains(text(), 'API')]")
                        except Exception:
                            pass
                    try:
                        for ont in active_ontologies:
                            if ont in driver.page_source.lower():
                                ontology="available"
                                ontologies = ontologies + ont
                    except Exception:
                        pass
                    try:
                        doi = driver.find_element_by_xpath("//*[contains(text(), 'doi')]")
                        doi.click()
                        print(driver.current_url)
                        doi = driver.find_element_by_class_name('epub-doi')
                    except Exception:
                        pass
                    if not doi:
                        try:
                            doi = driver.find_element_by_xpath("//*[contains(text(), 'doi')]")
                            doi.click()
                            print(driver.current_url)
                            doiTitle = driver.find_element_by_tag_name("title").get_attribute("textContent")
                            doi = ""
                        except Exception:
                            pass
                if not doi:
                    works = Works()
                    i=0
                    if doiTitle:
                        w1 = works.query(title=doiTitle).filter(type="journal-article").sort('relevance')
                        for item in w1:
                            i=i+1
                            if item['title'] is doiTitle:
                                doi = item['DOI']
                                break
                            if i > 10:
                                break
                    else:
                        w1 = works.query(title=search_phrase).filter(type="journal-article").sort("relevance")
                        for item in w1:
                            i=i+1
                            if search_phrase in item['title']:
                                doi = item['DOI']
                                break
                            if i > 10:
                                break
                if download:
                    downloadVal = 8.0
                else:
                    downloadVal = 0.0
                if publicRepo:
                    publicRepoVal = 8.0
                else:
                    publicRepoVal = 0.0
                if documentation:
                    documentationVal = 4.0
                else:
                    documentationVal = 0.0
                if versElem:
                    versVal = 2.0
                else:
                    versVal = 0.0
                compVal = 0.0
                if not windowsComp and not unixComp and not macComp:
                    compVal=0.0
                    winComp=0
                    unixComp=0
                    macComp=0
                else:
                    if windowsComp:
                        compVal = compVal + (5/3)
                        winComp=1.0
                    else:
                        winComp = 0.0
                    if unixComp:
                        compVal = compVal + (5/3)
                        unixComp=1.0
                    else:
                        unixComp=0.0
                    if macComp:
                        compVal = compVal + (5/3)
                        macComp=1.0
                    else:
                        macComp=0.0
                if about:
                    aboutVal = 5.0
                else:
                    aboutVal = 0.0
                if citeInfo:
                    citeVal = 2.0
                else:
                    citeVal = 0.0
                if contact:
                    contactVal = 2.0
                else:
                    contactVal = 0.0
                if apiInfo:
                    apiVal = 5.0
                else:
                    apiVal = 0.0
                if doi:
                    doiVal = 5.0
                else:
                    doiVal = 0.0
                if ontology:
                    ontologyVal = 4.0
                else:
                    ontologyVal = 0.0
                if source:
                    sourceVal = 5.0
                else:
                    sourceVal = 0.0
                if cli:
                    cliVal = 5.0
                else:
                    cliVal=0.0
                findability = ((downloadVal + doiVal + aboutVal + versVal) / (8+5+5+2)) * 100
                findability = round(findability, 2)
                accessiblity = ((apiVal+cliVal)/(5+5))*100
                accessiblity = round(accessiblity, 2)
                interoperability = ((compVal+sourceVal)/(5+5)) * 100
                interoperability = round(interoperability, 2)
                reusability = ((publicRepoVal + ontologyVal + documentationVal + contactVal + citeVal) / (8+4+4+2+2)) * 100
                tool = Tool.objects.create(tool_name=request.POST['name'], isPrivate=0)
                #tool = Tool.objects.get(tool_name = request.POST['name'])

                if doi:
                    doiShort = getBitlyLink(doi)
                if download:
                    downloadShort = getBitlyLink(download)
                if publicRepo:
                    publicRepoShort = getBitlyLink(publicRepo)

                fairScore = FairScore.objects.create(findability = findability, accessibility = accessiblity, interoperability = interoperability, reusability = reusability, tool_id = tool.id)
                find = Findability.objects.create(free_down=downloadVal, doi = doiVal, description = aboutVal, versions = versVal, tool_id=tool.id, doiLink=doi, downlink=download, shortDoiLink=doiShort, shortDownloadLink=downloadShort)
                acc = Accessibility.objects.create(api=apiVal, tool_id = tool.id, commandLine=cliVal)
                interop = Interoperability.objects.create(compatibility = compVal, tool_id=tool.id, macComp=macComp, unixComp=unixComp, winComp=winComp, sourceCode=sourceVal)
                reuse= Reusability.objects.create(public_repo=publicRepoVal, ontology=ontologyVal, documentation=documentationVal, contact=contactVal, citation=citeVal, tool_id=tool.id, repositoryLink=publicRepo, ontUsed=ontologies, usesOnt=1, shortRepoLink=publicRepoShort)
       
        return redirect('details', id=tool.id)
    return render(request, 'portal/add.html')