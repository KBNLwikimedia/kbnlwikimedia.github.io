# Resusing the album amicorum Jacob Heyblocq

This section is about **reusing AAJH content** (data & images, see [project page](https://www.wikidata.org/wiki/Wikidata:WikiProject_Alba_amicorum_National_Library_of_the_Netherlands/Jacob_Heyblocq)) that is stored in the Wikimedia infrastructure (= Wikidata + Wikimedia Commons + Wikipedia) in other (non-Wiki) sites, platforms, scripts, code, software etc.

## Contributors
* [See this page on Wikipedia](https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Topstukken/Hergebruik/Voorbeelden#Smoelenboek_van_de_bijdragers_aan_het_vriendenboek_van_Jacob_Heyblocq) for more context & explanations (in Dutch) 

### 1) HTML image gallery/smoelenboek based on the Wikimedia Commons API
Using its REST API, we want to simulate (parts of) the [Category:Contributors to the album amicorum Jacobus Heyblocq](https://commons.wikimedia.org/wiki/Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq) on Wikimedia Commons, which looks like this (dd 8-12-2020) [<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - Wikimedia Commons Category - 08-12-2020.png" width="600" align="left"/>](https://commons.wikimedia.org/wiki/Category:Contributors_to_the_album_amicorum_Jacobus_Heyblocq)
<br clear="all"/>
From the API we can create an [image gallery/smoelenboek of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-CommmonsAPI.html) in HTML, using this [python-script](https://github.com/KBNLwikimedia/AlbumAmicorumJacobHeyblocq/blob/master/reuse/scripts/bijdragersAAJH-smoelenboek-CommonsAPI.py) to generate this image gallery.  

[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - CommmonsAPI - 31-12-2020.png" width="600" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-CommmonsAPI.html)

<br clear="all"/>

### 2) SPARQL-query op Wikidata
<br clear="all"/>

### 3) SPARQL-query met JSON-response
<br clear="all"/>

### 4) Mockups for integrating Wikidata SPARQL query results into kb.nl using HTML iframe
* [Image gallery / smoelenboek of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-mockupkbnl.html) 
* [List of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-lijst-SparqlHTMLembed-mockupkbnl.html)
* [Occupations cloud of contributors](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-beroepen-SparqlHTMLembed-mockupkbnl.html) 

[<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Smoelenboek - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250" align="left"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-smoelenboek-SparqlHTMLembed-mockupkbnl.html) [<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Lijst - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-lijst-SparqlHTMLembed-mockupkbnl.html) [<img src="https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/images/Contributors to the album amicorum Jacobus Heyblocq - Beroepenwolk - SparqlHTMLembed-mockupkbnl - 31-12-2020.png" height="250"/>](https://kbnlwikimedia.github.io/AlbaAmicorum/AlbumAmicorumJacobHeyblocq/reuse/bijdragersAAJH-beroepen-SparqlHTMLembed-mockupkbnl.html )
