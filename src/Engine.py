# Import library to scrap the people also ask from Google Search Engine
import people_also_ask
import urllib.parse
# Method
def search(search_term,item=5):
    """ method to search from the google and organize the output """
    try:
        paa=people_also_ask.get_related_questions(search_term,item+1)
        output=[]
        for i in paa:
            response=people_also_ask.get_answer(i)
            if response.get("has_answer")==True:
                res = dict((k, response[k]) for k in ['question','response','displayed_link','link','title'] if k in response)
                res1=urllib.parse.unquote(res.get("link"))
                res["link"]=res1
                output.append(res)
            else:
                pass
    except:
        output=[]
    return(output)
