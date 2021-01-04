# Resusing the album amicorum Jacob Heyblocq

This section is about **reusing AAJH content** (data & images, see [project page](https://www.wikidata.org/wiki/Wikidata:WikiProject_Alba_amicorum_National_Library_of_the_Netherlands/Jacob_Heyblocq)) that is stored in the Wikimedia infrastructure (= Wikidata + Wikimedia Commons + Wikipedia) in other (non-Wiki) sites, platforms, scripts, code, software etc.

## Contributors
[See the corresponding page on Dutch Wikipedia](https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden#Smoelenboek_van_de_bijdragers_aan_het_vriendenboek_van_Jacob_Heyblocq) for more context & explanations (in Dutch) 

### 1) HTML image gallery/smoelenboek based on the Wikimedia Commons API
Using its REST API, we want to mimick (parts of) the [Category:Contributors to the album amicorum Jacobus Heyblocq](https://commons.wikimedia.org/wiki/Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq) on Wikimedia Commons. This category looks like this (dd 8-12-2020) 

[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - Wikimedia Commons Category - 08-12-2020.png" width="800" align="left"/>](https://commons.wikimedia.org/wiki/Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq)
<br clear="all"/>

From the [JSON response of the API](https://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmlimit=500&gcmnamespace=6&gcmtitle=Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq&format=json) and using this [Python script](scripts/bijdragersAAJH-smoelenboek-CommonsAPI.py) we can generate a [basic HTML image gallery/smoelenboek of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-CommmonsAPI.html). The resulting HTML page looks like this:

[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - CommmonsAPI - 31-12-2020.png" width="800" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-CommmonsAPI.html)
<br clear="all"/>

Disadvantage of this approach: Wikimedians can adjust categorizations on Commons as they see fit. As a result, images can disappear from the above API call, or multiple images of 1 particular contributor can appear in the JSON response. In other words, the number of images in the resulting facebook can change, without one noticing.

### 2) SPARQL-query op Wikidata
<br clear="all"/>

### 3) HTML image gallery/smoelenboek based on the Wikidata SPARQL API with JSON-response
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

[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - SparqlWikidataJson - 01-01-2021.png" width="800" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlWikidataJson.html)
<br clear="all"/>

### 4) Mockups for integrating Wikidata SPARQL query results into kb.nl using HTML iframe
* [Image gallery / smoelenboek of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-mockupkbnl.html) 
* [List of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-lijst-SparqlHTMLembed-mockupkbnl.html)
* [Occupations cloud of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-beroepen-SparqlHTMLembed-mockupkbnl.html) 

[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-mockupkbnl.html) [<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Lijst - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-lijst-SparqlHTMLembed-mockupkbnl.html) [<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Beroepenwolk - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-beroepen-SparqlHTMLembed-mockupkbnl.html )
