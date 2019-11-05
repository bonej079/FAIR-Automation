from googleapiclient.discovery import build
from selenium import webdriver
from crossref.restful import Works, Journals
import requests


my_api_key = "AIzaSyAqqbU_8-csEQuknlFfEfccDnviAXSpH9o"
my_cse_id = "010537144392431308903:g2eqgue84js"
search_phrase = "[Name of Dataset]"
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
persistent = ""
fileformat = ""
about = ""
versElem = ""
citeInfo = ""
contact = ""
doi = ""
doiTitle=""
# print(link)

if link:
    driver.get(link)
    
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
                    persistent = "available"
                    break
                if i > 10:
                    break
        else:
            w1 = works.query(title=search_phrase).filter(type="journal-article").sort("relevance")
            for item in w1:
                i=i+1
                if search_phrase in item['title']:
                    doi = item['DOI']
                    persistent = "available"
                    break
                if i > 10:
                    break
    
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
        elem = driver.find_element_by_partial_link_text("Download")
        download = "available"
    except Exception:
        pass

    if not fileformat:
        try:    
            fileformat = driver.find_element_by_xpath("//*[contains(text(), 'file format')]")
        except Exception:
            pass
            
        if not fileformat:
            try:
                fileformat = driver.find_element_by_xpath("//*[contains(text(), 'format')]")
            except Exception:
                pass

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
            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Citation')]")
        except Exception:
            pass

    if not citeInfo:
        try:
            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Cite')]")
        except Exception:
            pass

    if not citeInfo:
        try:
            citeInfo = driver.find_element_by_xpath("//*[contains(text(), 'Publications')]")
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

print("========================================================================")

if download:
    print("Dataset can be downloaded.")
    downloadVal = 8.0
else:
    print("Dataset cannot be downloaded.")
    downloadVal = 0.0

if versElem:
    print("Previous versions of dataset available.")
    versVal = 5.0
else:
    print("Previous versions of dataset not available.")
    versVal = 0.0

if about:
    print("Dataset description given.")
    aboutVal = 6.0
else:
    print("No dataset description found.")
    aboutVal = 0.0

if citeInfo:
    print("Information on how to cite dataset is given.")
    citeVal = 5.0
else:
    print("No information found on how to cite dataset.")
    citeVal = 0.0

if contact:
    print("Developer's contact information given.")
    contactVal = 5.0
else:
    print("No contact information found.")
    contactVal = 0.0

if fileformat:
    print("Dataset file format information provided.")
    fileVal = 10.0
else:
    print("Dataset file format information not provided.")
    fileVal = 0.0

if doi:
    print("DOI of dataset found.")
    doiVal = 4.0
else:
    print("No DOI found.")
    doiVal = 0.0

if persistent:
    print("Dataset will persist.")
    persVal = 2.0
else:
    print("Dataset will not persist.")
    persVal=0.0

findability = ((doiVal + aboutVal) / (6+4)) * 100
findability = round(findability, 2)

accessiblity = ((downloadVal+persVal)/(8+2))*100
accessiblity = round(accessiblity, 2)

interoperability = ((fileVal)/(10)) * 100
interoperability = round(interoperability, 2)

reusability = ((versVal + contactVal + citeVal) / (5+5+5)) * 100
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
print(contactVal)
print(citeVal)
print(persVal)
print(fileVal)