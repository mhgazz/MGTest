import requests
import json

tc = 0
f = open("testcases.csv", "r")
for tcase in f :
    tc = tc + 1 
    lcase = tcase.split(",");
    searchq = lcase[0]
    expt_position = int(lcase[1])-1
    expt_result = lcase[2]
    url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyB6R-g3AYlpvCec6kFs0Nbk2of5Ues33oY&cx=014465205443203265746:sx2fgoft8qp&q=" + searchq 
    google_result = json.loads(requests.get(url).text)
    result = google_result["items"][int(expt_position)]["title"]
    print "-------------\r\ntest case " + str(tc)
    if(result[0:30].lower() == expt_result[0:30].lower()):
        print "test succeded"
    else:
        print "test failed"
        print "actual: " + result
        print "expected: " + expt_result

