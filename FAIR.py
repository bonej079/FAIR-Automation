from googleapiclient.discovery import build
from selenium import webdriver
from crossref.restful import Works, Journals
import requests
import yaml

active_ontologies = []

with open("ontologies.yml", 'r') as ont:
    try:
        content = yaml.load(ont)
        for item in content.items():
            x = item[1]
            for i in range(len(x)):
                if x[i]["activity_status"] == "active":
                    active_ontologies.append(x[i]["title"].lower())
    except yaml.YAMLError as exc:
        print(exc)

# print(active_ontologies)

my_api_key = "AIzaSyAqqbU_8-csEQuknlFfEfccDnviAXSpH9o"
my_cse_id = "010537144392431308903:g2eqgue84js"
search_phrase = "[Name of Tool]"
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
source = ""
cli = ""
git= ""
# print(link)

if link:
    driver.get(link)
    try:
        elem = driver.find_element_by_partial_link_text("Download")
        download = "available"
        elem.click()  
    except Exception:
        pass

    if "github.com" in driver.current_url:
        # print("public resource available")
        publicRepo = "available"
        documentation = "available"
        download = "available"
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
            publicRepo = "available"
            documentation = "available"
            download="available"
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
            publicRepo = "available"
            documentation = "available"
            download = "available"
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
                publicRepo = "available"
                documentation = "available"
                download="available"
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
                ontologies = ont
    except Exception:
        pass

    try:
        doi = driver.find_element_by_xpath("//*[contains(text(), 'doi')]")
        doi.click()
        print(driver.current_url)
        doi = driver.find_element_by_class_name('epub-doi')
        print(doi.text)
    except Exception:
        pass
    if not doi:
        try:
            doi = driver.find_element_by_xpath("//*[contains(text(), 'doi')]")
            doi.click()
            print(driver.current_url)
            doiTitle = driver.find_element_by_tag_name("title").get_attribute("textContent")
            doi = ""
            print(doiTitle)
        except Exception:
            pass

if not doi:
    works = Works()
    i=0
    if doiTitle:
        print(doiTitle)
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

else:
    print(doi)

print("========================================================================")

if download:
    print("Tool can be downloaded.")
    downloadVal = 8.0
else:
    print("Tool cannot be downloaded.")
    downloadVal = 0.0

if publicRepo:
    print("Public repository available.")
    publicRepoVal = 8.0
else:
    print("No public repository found.")
    publicRepoVal = 0.0

if documentation:
    print("Tool documentation available.")
    documentationVal = 4.0
else:
    print("No tool documentation found.")
    documentationVal = 0.0

if versElem:
    print("Previous versions of tool available.")
    versVal = 2.0
else:
    print("Previous versions of tool not available.")
    versVal = 0.0

compVal = 0.0
if not windowsComp and not unixComp and not macComp:
    print("No OS compatibility information given.")
else:
    if windowsComp:
        print("Tool is compatible with Windows.")
        compVal = compVal + (5/3)
    if unixComp:
        print("Tool is compatible with UNIX systems.")
        compVal = compVal + (5/3)
    if macComp:
        print("Tool is compatible with MAC OS.")
        compVal = compVal + (5/3)

if about:
    print("Tool description given.")
    aboutVal = 5.0
else:
    print("No tool description found.")
    aboutVal = 0.0

if citeInfo:
    print("Information on how to cite tool is given.")
    citeVal = 2.0
else:
    print("No information found on how to cite tool.")
    citeVal = 0.0

if contact:
    print("Developer's contact information given.")
    contactVal = 2.0
else:
    print("No contact information found.")
    contactVal = 0.0

if apiInfo:
    print("Tool supports API usage.")
    apiVal = 5.0
else:
    print("No information found on API usage.")
    apiVal = 0.0

if doi:
    print("DOI of tool found.")
    doiVal = 5.0
else:
    print("No DOI found.")
    doiVal = 0.0

if ontology:
    print("Tool uses a community accepted ontology.")
    ontologyVal = 4.0
else:
    print("Tool does not use an ontology, or no information was given on what ontologies are used.")
    ontologyVal = 0.0

if source:
    print("Tool source code available.")
    sourceVal = 5.0
else:
    print("Tool source code not available.")
    sourceVal = 0.0

if cli:
    print("Information about command line available.")
    cliVal = 5.0
else:
    print("No information about command line available.")
    cliVal=0.0

findability = ((downloadVal + doiVal + aboutVal + versVal) / (8+5+5+2)) * 100
findability = round(findability, 2)

accessiblity = ((apiVal+cliVal)/(5+5))*100
accessiblity = round(accessiblity, 2)

interoperability = ((compVal+sourceVal)/(5+5)) * 100
interoperability = round(interoperability, 2)

reusability = ((publicRepoVal + ontologyVal + documentationVal + contactVal + citeVal) / (8+4+4+2+2)) * 100
reusability = round(reusability, 2)

print("==============================")
print("Findability: "+str(findability) + "%")
print("Accessiblity:"+str(accessiblity) + "%")
print("Interoperability:"+str(interoperability) + "%")
print("Reusability:"+str(reusability) + "%")

print("===============================")
print(downloadVal)
print(doiVal)
print(aboutVal)
print(versVal)
print(apiVal)
print(compVal)
print(publicRepoVal)
print(ontologyVal)
print(documentationVal)
print(contactVal)
print(citeVal)
print(sourceVal)
print(cliVal)