import urllib.request
import urllib.parse
import re

#function to generate URL from text query_string
def generateRUL(str):
    query_string = urllib.parse.urlencode({"search_query" : str })
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    search_result = "http://www.youtube.com/watch?v=" + search_results[0]
    return search_result
#end : def generateRUL
