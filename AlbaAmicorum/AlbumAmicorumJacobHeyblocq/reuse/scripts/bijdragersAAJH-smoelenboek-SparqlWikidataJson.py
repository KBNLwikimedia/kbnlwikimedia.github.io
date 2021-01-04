# Basic script for
# https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden/Smoelenboek_bijdragers_AAJH#4)_SPARQL-query_op_Wikidata_met_JSON-respons

# We request data about the contributors to the album amicorum from the SPARQL endpoint on Wikidata via
# https://w.wiki/soe

# SELECT DISTINCT ?contributor ?contributorLabel ?contributorDescription ?image ?commonscat ?wparticleNL WHERE {
#  BIND(wd:Q72752496 as ?album)
#  ?album wdt:P767 ?contributor.
#  ?contributor wdt:P18 ?image.
#  OPTIONAL{?contributor wdt:P373 ?commonscat.}
#  OPTIONAL{?wparticleNL schema:about ?contributor.
#           ?wparticleNL schema:isPartOf <https://nl.wikipedia.org/>.}
#  SERVICE wikibase:label { bd:serviceParam wikibase:language "nl". }
# }
# ORDER BY ?contributorLabel

# Or, the above query with a json response:
# https://query.wikidata.org/sparql?query=SELECT%20DISTINCT%20%3Fcontributor%20%3FcontributorLabel%20%3FcontributorDescription%20%3Fimage%20%3Fcommonscat%20%3FwparticleNL%20WHERE%20%7B%20%0A%20%20BIND(wd%3AQ72752496%20as%20%3Falbum)%0A%20%20%3Falbum%20wdt%3AP767%20%3Fcontributor.%0A%20%20%3Fcontributor%20wdt%3AP18%20%3Fimage.%0A%20%20OPTIONAL%7B%3Fcontributor%20wdt%3AP373%20%3Fcommonscat.%7D%0A%20%20OPTIONAL%7B%3FwparticleNL%20schema%3Aabout%20%3Fcontributor.%0A%20%20%20%20%20%20%20%20%20%20%20%3FwparticleNL%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fnl.wikipedia.org%2F%3E.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22nl%22.%20%7D%0A%7D%20%0AORDER%20BY%20%3FcontributorLabel&format=json

# We process this json into a basic image thumb gallery (facebook, Dutch:smoelenboek) in HTML, using the Python script below

######################################################################
import json
import requests
import hashlib
import urllib.parse
from bs4 import BeautifulSoup

HTMLtemplate ="""
<html>
<head>
<!-- # HTML smoelenboek bij https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden#4)_SPARQL-query_op_Wikidata_met_JSON-respons --> 
<meta http-equiv="content-type" content="text/html;charset=utf-8"/>
<link rel="stylesheet" href="./css/bijdragersAAJH-smoelenboek.css"> 
<title>Smoelenboek bijdragers vriendenboek Jacob Heyblocq - Demo o.b.v. SPARQL-query op Wikidata met JSON-respons</title>
</head>
<body>
<h1>Smoelenboek bijdragers <a href="https://www.kb.nl/themas/vriendenboeken/verwoede-verzamelaars/jacob-heyblocqs-vriendenboek" 
target="_blank">Vriendenboek Jacob Heyblocq</a> - Demo o.b.v. SPARQL-query op Wikidata met JSON-respons</h1>
<ul>
<li>SPARQL query op Wikidata: <a href="https://w.wiki/soe" target="_blank">https://w.wiki/soe</a></li>
<li>Uitleg & context in het Nederlands, op Wikipedia: <a href="https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden#4)_SPARQL-query_op_Wikidata_met_JSON-respons" target="_blank">https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden#4)_SPARQL-query_op_Wikidata_met_JSON-respons</a></li>
<li>Uitleg & context in het Engels, op Github: <a href="https://github.com/KBNLwikimedia/kbnlwikimedia.github.io/blob/master/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse" 
target="_blank">https://github.com/KBNLwikimedia/kbnlwikimedia.github.io/blob/master/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse</a></li>
</ul>
<div class="fiveColumnGrid">
{gallery}
</div>
</body>
</html>
"""
#######################################
gallery = ""
wmc_baseurl="https://commons.wikimedia.org/wiki/"
wmc_jsonurl = "https://query.wikidata.org/sparql?query=SELECT%20DISTINCT%20%3Fcontributor%20%3FcontributorLabel%20%3FcontributorDescription%20%3Fimage%20%3Fcommonscat%20%3FwparticleNL%20WHERE%20%7B%20%0A%20%20BIND(wd%3AQ72752496%20as%20%3Falbum)%0A%20%20%3Falbum%20wdt%3AP767%20%3Fcontributor.%0A%20%20%3Fcontributor%20wdt%3AP18%20%3Fimage.%0A%20%20OPTIONAL%7B%3Fcontributor%20wdt%3AP373%20%3Fcommonscat.%7D%0A%20%20OPTIONAL%7B%3FwparticleNL%20schema%3Aabout%20%3Fcontributor.%0A%20%20%20%20%20%20%20%20%20%20%20%3FwparticleNL%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fnl.wikipedia.org%2F%3E.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22nl%22.%20%7D%0A%7D%20%0AORDER%20BY%20%3FcontributorLabel&format=json"

r = requests.get(wmc_jsonurl)
data = json.loads(r.content) # utf-8, see https://stackoverflow.com/questions/44203397/python-requests-get-returns-improperly-decoded-text-instead-of-utf-8
contribs = list(data['results']['bindings'])
#print(contribs)

for c in contribs:
    print("------------------------------------------")
    if c.get('contributor', 'aa') != 'aa':
        contributor = c.get('contributor').get('value')
        print(f"contributor: {contributor}")
    if c.get('contributorLabel', 'aa') != 'aa':
        contributorLabel = c.get('contributorLabel').get('value')
        print(f"contributorLabel: {contributorLabel}")
    if c.get('contributorDescription', 'aa') != 'aa':
        contributorDescription = c.get('contributorDescription').get('value')
        print(f"contributorDescription : {contributorDescription}")
    if c.get('image', 'aa') != 'aa':
        contributorImage = c.get('image').get('value')
        print(f"contributorImage : {contributorImage}")

    # Full image : http://commons.wikimedia.org/wiki/Special:FilePath/Portret%20van%20Robertus%20Keuchenius%2C%20RP-P-1906-1594.jpg
    # From https://www.mediawiki.org/wiki/Topic:Pzvu1613ewnfahcd :
    # Thumb 300px wide: http://commons.wikimedia.org/wiki/Special:FilePath/Portret%20van%20Robertus%20Keuchenius%2C%20RP-P-1906-1594.jpg?width=300
    thumbwidth='300'
    contributorThumb = f"{contributorImage}?width={thumbwidth}"
    print(f"contributorThumb: {contributorThumb}")

    contributorPage = wmc_baseurl + "File:" + str(contributorImage.split("FilePath/")[1])
    print(f"contributorPage: {contributorPage}")

    ## Get Commons category and Dutch WP article
    if c.get('commonscat', 'aa') != 'aa': #There is a commons cat for this contributor
        contributorCommonscat = c.get('commonscat').get('value')
    else: contributorCommonscat = 'XXX'
    print(f"contributorCommonscat: {wmc_baseurl}Category:{contributorCommonscat.replace(' ', '_')}")

    if c.get('wparticleNL', 'aa') != 'aa': #There is a Dutch WP article
        contributorWParticleNL = c.get('wparticleNL').get('value')
    else: contributorWParticleNL = 'XXX'
    print(f"contributorWParticleNL: {contributorWParticleNL}")

    ### Now build the image gallery / smoelenboek
    gallery += f"<figure class='fiveColumnGridItem'><a target='_blank' href='{contributorPage}'>" \
               f"<img src='{contributorThumb}' alt='{contributorLabel}'/></a>" \
               f"<figurecaption><b>{contributorLabel}</b><br/>{contributorDescription}<br/><br/>"
    if contributorWParticleNL != 'XXX': #There is a Dutch WP article
        gallery += f"<li><a target='_blank' href='{contributorWParticleNL}'>Wikipedia</a></li>"
    if contributorCommonscat != 'XXX': #There is a Commons category for this contributor
        gallery += f"<li><a target='_blank' href='{wmc_baseurl}Category:{contributorCommonscat.replace(' ', '_')}'>Commons</a></li>"
    gallery += f"<li><a target='_blank' href='{contributor}'>Wikidata</a></li>"
    gallery +=f"</figurecaption></figure>"

html = HTMLtemplate.format(gallery=gallery)
soup = BeautifulSoup(html, 'html.parser')
prettyHTML = soup.prettify()
HTMLoutputfile = open("../bijdragersAAJH-smoelenboek-SparqlWikidataJson.html", "w", encoding='utf-8')
HTMLoutputfile.write(prettyHTML)
HTMLoutputfile.close()
