# Resusing the album amicorum Jacob Heyblocq

This section is about **reusing AAJH content** (data & images, see [project page](https://www.wikidata.org/wiki/Wikidata:WikiProject_Alba_amicorum_National_Library_of_the_Netherlands/Jacob_Heyblocq)) that is stored in the Wikimedia infrastructure (= Wikidata + Wikimedia Commons + Wikipedia) in other (non-Wiki) sites, platforms, scripts, code, software etc.

## Image gallery of album contributors
**[>> See the corresponding page on Dutch Wikipedia](https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden/Smoelenboek_bijdragers_AAJH)** for additional context & explanations (in Dutch). 

[Dozens of people](https://www.kb.nl/themas/vriendenboeken/verwoede-verzamelaars/jacob-heyblocqs-vriendenboek) (see the bottom of that page, at *Index op auteursnamen*) contributed to the 17th century [album amicorum of Jacob Heyblocq](https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Alfabetisch#Album_amicorum_van_Jacobus_Heyblocq_(1623-1690),_rector_van_de_Latijnse_school_te_Amsterdam). We would like to make a photo gallery/facebook (Dutch: *smoelenboek*) of these persons, as far as images of those persons are known (on Commons).

We can do this in multiple ways:

### 1) HTML image gallery/smoelenboek based on the Wikimedia Commons API
Using its REST API, we want to mimick (parts of) the [Category:Contributors to the album amicorum Jacobus Heyblocq](https://commons.wikimedia.org/wiki/Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq) on Wikimedia Commons. This category looks like this (dd 8-12-2020) 

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - Wikimedia Commons Category - 08-12-2020.png" width="800" align="left"/>](https://commons.wikimedia.org/wiki/Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq)</kbd>
<br clear="all"/>

From the [JSON response of the API](https://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmlimit=500&gcmnamespace=6&gcmtitle=Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq&format=json) and using this [Python script](scripts/bijdragersAAJH-smoelenboek-CommonsAPI.py) we can generate a [basic HTML image gallery/smoelenboek of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-CommmonsAPI.html). The resulting HTML page looks like this:

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - CommmonsAPI - 31-12-2020.png" width="800" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-CommmonsAPI.html)</kbd>
<br clear="all"/>

Disadvantage of this approach: Wikimedians can adjust categorizations on Commons as they see fit. As a result, images can disappear from the above API call, or multiple images of 1 particular contributor can appear in the JSON response. In other words, the number of images in the resulting facebook can change, without one noticing.

### 2) SPARQL query on Wikidata
In the Wikidata item *[Album amicorum of Jacobus Heyblocq (1623-1690), rector of the Latin school in Amsterdam (Q72752496)](https://www.wikidata.org/wiki/Q72752496)*, all contributors to this album are included in the property [contributor to the creative work or subject (P767)](https://www.wikidata.org/wiki/Property:P767). As a result, we can gather all those persons using [the SPARQL query below](https://w.wiki/tBE) and then display their images/faces in a ready-made gallery in the Wikidata interface

```
#defaultView:ImageGrid{"hide":["?gender","?portrait"]}
SELECT DISTINCT ?contributorDescription ?contributor ?contributorLabel ?gender ?portrait WHERE { 
  BIND(wd:Q72752496 as ?album)
  ?album wdt:P767 ?contributor.
  ?contributor wdt:P21 ?gender.
  OPTIONAL{?contributor wdt:P18 ?image.}
  
  BIND (wd:Q82985930 as ?maledummy) 
  BIND (wd:Q82992173 as ?femaledummy)  
  ?maledummy wdt:P18 ?maledummyimage.
  ?femaledummy wdt:P18 ?femaledummyimage.
  BIND(IF(?gender=wd:Q6581072,?femaledummyimage,?maledummyimage) as ?dummyimage). #Choose the dummyimage dependent on gender (female/male)
  BIND(IF(BOUND(?image), ?image,?dummyimage) as ?portrait). #If no image is known, substitute the dummy image
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,nl". }
} 
ORDER BY DESC (?image)
```
Here, via [Q82985930](https://www.wikidata.org/wiki/Q82985930) + *?maledummyimage* and [Q82992173](https://www.wikidata.org/wiki/Q82992173) + *?femaledummyimage*, male and female dummy images are inserted for the male resp. female album contributors whose images are not known in Wikimedia Commons.

The 'smoelenboek' as a result of the above query looks like this:

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - Wikidata SPARQL gallery - 08-12-2020.PNG" width="800" align="left"/>](https://w.wiki/phx)</kbd>
<br clear="all"/>

### 3) HTML image gallery/smoelenboek based on the Wikidata SPARQL API with JSON response
When runnuing a SPARQL query in the Wikidata query interface, we have the result displayed directly (out of the box) in that interface, as shown above. However, we can also request the search result as a JSON response and then build a custom/DIY interface with it ourselves. We do this as follows:

1) Using [the SPARQL query below](https://w.wiki/soe), we first request some data about the album contributors directly in the Wikidata interface

```
SELECT DISTINCT ?contributor ?contributorLabel ?contributorDescription ?image ?commonscat ?wparticleNL WHERE { 
  BIND(wd:Q72752496 as ?album)
  ?album wdt:P767 ?contributor.
  ?contributor wdt:P18 ?image.
  OPTIONAL{?contributor wdt:P373 ?commonscat.}
  OPTIONAL{?wparticleNL schema:about ?contributor.
           ?wparticleNL schema:isPartOf <https://nl.wikipedia.org/>.}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "nl". }
} 
ORDER BY ?contributorLabel
```

So we request
- the Wikidata Q number (?contributor),
- the name, the Dutch description and the image (but now without the dummy images),
- the Dutch Wikipedia article and the Commons category (if available)

of the contributors, because we want to display this data in the DIY interface.

2) Once we have checked that the query and search results are OK, we then request the same response in JSON:

<sub>https://query.wikidata.org/sparql?query=SELECT%20DISTINCT%20%3Fcontributor%20%3FcontributorLabel%20%3FcontributorDescription%20%3Fimage%20%3Fcommonscat%20%3FwparticleNL%20WHERE%20%7B%20%0A%20%20BIND(wd%3AQ72752496%20as%20%3Falbum)%0A%20%20%3Falbum%20wdt%3AP767%20%3Fcontributor.%0A%20%20%3Fcontributor%20wdt%3AP18%20%3Fimage.%0A%20%20OPTIONAL%7B%3Fcontributor%20wdt%3AP373%20%3Fcommonscat.%7D%0A%20%20OPTIONAL%7B%3FwparticleNL%20schema%3Aabout%20%3Fcontributor.%0A%20%20%20%20%20%20%20%20%20%20%20%3FwparticleNL%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fnl.wikipedia.org%2F%3E.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22nl%22.%20%7D%0A%7D%20%0AORDER%20BY%20%3FcontributorLabel&format=json</sub>

3) With this JSON we can now use [this Python script](https://github.com/KBNLwikimedia/kbnlwikimedia.github.io/blob/master/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/scripts/bijdragersAAJH-smoelenboek-SparqlWikidataJson.py) create [this simple HTML photo gallery/smoelenboek](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlWikidataJson.html). It looks like this:

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - SparqlWikidataJson - 01-01-2021.png" width="800" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlWikidataJson.html)</kbd>

### 4) Wikidata SPARQL + HTML-embed via iframe
The facebook made above (see 2) can also be embedded in an HTML page by means of an HTML iframe. The basic code for that looks like this:

  ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Smoelenboek van de bijdragers aan het vriendenboek van Jacob Heyblocq - Wikidata SPARQL + HTML iframe</title>
    </head>
    <body>
    	<h1>Smoelenboek van de bijdragers aan het vriendenboek van Jacob Heyblocq - Wikidata SPARQL + HTML iframe</h1>
    	<iframe style="position: absolute; height: 100%; width: 100%; border: none" src="https://query.wikidata.org/embed.html#%23defaultView%3AImageGrid%7B%22hide%22%3A%5B%22%3Fgender%22%2C%22%3Fportrait%22%5D%7D%0ASELECT%20DISTINCT%20%3FcontributorDescription%20%3Fcontributor%20%3FcontributorLabel%20%3Fgender%20%3Fportrait%20WHERE%20%7B%20%0A%20%20BIND(wd%3AQ72752496%20as%20%3Falbum)%0A%20%0A%20%20%3Falbum%20wdt%3AP767%20%3Fcontributor.%0A%20%20%3Fcontributor%20wdt%3AP21%20%3Fgender.%0A%20%20OPTIONAL%7B%3Fcontributor%20wdt%3AP18%20%3Fimage.%7D%0A%0A%20%20BIND%20(wd%3AQ82985930%20as%20%3Fmaledummy)%20%0A%20%20BIND%20(wd%3AQ82992173%20as%20%3Ffemaledummy)%20%20%0A%20%20%3Fmaledummy%20wdt%3AP18%20%3Fmaledummyimage.%0A%20%20%3Ffemaledummy%20wdt%3AP18%20%3Ffemaledummyimage.%0A%20%20BIND(IF(%3Fgender%3Dwd%3AQ6581072%2C%3Ffemaledummyimage%2C%3Fmaledummyimage)%20as%20%3Fdummyimage).%20%23Choose%20the%20dummyimage%20dependent%20on%20gender%20(female%2Fmale)%0A%20%20%20%0A%20%20BIND(IF(BOUND(%3Fimage)%2C%20%3Fimage%2C%3Fdummyimage)%20as%20%3Fportrait).%20%23If%20no%20image%20is%20known%2C%20substitute%20the%20dummy%20image%0A%20%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cnl%22.%20%7D%0A%7D%20%0AORDER%20BY%20DESC%20(%3Fimage)" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>
    </body>
</html>
```
This gives a [plain, unstyled smoelenboek](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-plain.html) looking like this: 

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - SparqlHTMLembed-plain - 04-01-2021.png" width="800" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-plain.html)</kbd>

#### kb.nl styling
We can further develop this HTML iframe approach into a design that fits seamlessly into [the pages about the album on the KB website](https://www.kb.nl/themas/vriendenboeken/verwoede-verzamelaars/jacob-heyblocqs-vriendenboek), resulting into [an HTML-page](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-mockupkbnl.html) looking like this:

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" width="800" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-mockupkbnl.html)</kbd>

In addition to this image gallery, we can also make [a list](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-lijst-SparqlHTMLembed-mockupkbnl.html) and a [cloud of professions](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-beroepen-SparqlHTMLembed-mockupkbnl.html) of the album contributors in the design of kb.nl, again based on embedded HTML iframes containing Wikidata SPARQL queries:

<kbd>[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Lijst - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-lijst-SparqlHTMLembed-mockupkbnl.html) [<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Beroepenwolk - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-beroepen-SparqlHTMLembed-mockupkbnl.html)</kbd>
