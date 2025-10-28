<table width="100%" border="0"><tr><td align="left">
<a href="https://kbnlwikimedia.github.io/"><< Back to homepage</a>
</td><td align="right">
<a href="https://github.com/KBNLwikimedia/kbnlwikimedia.github.io" target="_blank">>> To the Github repo of this page</a>
</td></tr></table>
<hr/>

<img src="../media/KB_Nationale-Bibliotheek_Logo_RGB-Zwart-EN.png" width="350" hspace="0" align="left"/>
<img src="../media/wikimedia-logos.png" align="right" width="300" hspace="0" align="left"/>
<br clear="all"/>

<img src="../media/screwdriver-wrench.svg" align="left" width="100" hspace="20" vspace="10"/>

# Overview of tools and scripts on Github related to the Wikimedia effort of the KB
<br clear="all"/>

## Wikimedia Commons tools

### [GLAMorousToHTML](https://kbnlwikimedia.github.io/GLAMorousToHTML/)
Creates a datestamped HTML report and a corresponding Excel file listing all Wikipedia articles (in all languages) in which (one or more) images from a given category tree on Wikimedia Commons are used. 
* [GLAM reports](https://kbnlwikimedia.github.io/GLAMorousToHTML/reports/reports.html) created by this tool
* [Github repo](https://github.com/KBNLwikimedia/GLAMorousToHTML)
* [Tool page on Commons](https://commons.wikimedia.org/wiki/Commons:GLAMorousToHTML)
* [Commons category](https://commons.wikimedia.org/wiki/Category:GLAMorousToHTML)
* Story: [Public outreach and reuse of KB images via Wikipedia, 2014-2022](https://kbnlwikimedia.github.io/GLAMorousToHTML/stories/Public%20outreach%20and%20reuse%20of%20KB%20images%20via%20Wikipedia%2C%202014-2022.html)
* <a href="https://kbnlwikimedia.github.io/GLAMorousToHTML/extras/delpher_humans_q5_gallery.html" target="_blank"><image src="https://kbnlwikimedia.github.io/GLAMorousToHTML/extras/media/wikipedia-delpher-portrait-explorer_20250912.jpg" hspace="10" align="right" width="200"/></a>
Prototype: [Wikipedia ❤️ Delpher - Portrait explorer](https://kbnlwikimedia.github.io/GLAMorousToHTML/extras/delpher_humans_q5_gallery.html), a visual exploration of notable individuals in Wikipedia, illustrated by Delpher.<br/>
 It allows you to explore humans who are described in Wikipedia articles illustrated by [Delpher images](https://commons.wikimedia.org/wiki/Category:Media_from_Delpher). You can do so by occupation, gender, country of citizenship, decades of birth and death and Wikipedia language version. For instance: a [female opera singer from France born in the 1880s described by a Wikipedia article in French](https://kbnlwikimedia.github.io/GLAMorousToHTML/extras/delpher_humans_q5_gallery.html?page=1&sort=name_asc&country=Q142&gender=Q6581072&occ=Q2865819&dob=1880&pc=fr).<br/>

### [Wikimedia Commons File Metadata Downloader](https://github.com/KBNLwikimedia/wikimedia-various-tools/tree/main/wmc-metadata-downloader)
Collect metadata from Wikimedia Commons files or categories and write them into an Excel sheet — safely, in chunks, and with per-file JSON snapshots.
* [Github repo](https://github.com/KBNLwikimedia/wikimedia-various-tools/tree/main/wmc-metadata-downloader)

### [Wikimedia Commons File Downloader](https://github.com/KBNLwikimedia/wikimedia-various-tools/tree/main/wmc-file-downloader)
A robust, Windows-safe downloader for Wikimedia Commons files - Download Wikimedia Commons files by nested category tree or flat list, preview before downloading, slice a subset, use Windows-safe unique filenames, and log to Excel.
* [Github repo](https://github.com/KBNLwikimedia/wikimedia-various-tools/tree/main/wmc-file-downloader)

### [Wikimedia Commons URL M-ID Excel Extractor](https://github.com/KBNLwikimedia/wikimedia-various-tools/tree/main/wmc-url-mid-excel-extractor)
Reads a Wikimedia Commons FileURL column from an Excel sheet, looks up the corresponding MediaInfo entity IDs (M-IDs), and writes the results back into the same Excel workbook.
* [Github repo](https://github.com/KBNLwikimedia/wikimedia-various-tools/tree/main/wmc-url-mid-excel-extractor)

### [Wikimedia Commons copyright template extractor](https://kbnlwikimedia.github.io/wikimedia-commons_copyright-templates/)
Identifies public domain (PD) or PD-like (Creative Commons) license templates in Wikimedia Commons files, alongside simplified creation/publication dates.
* [Github repo](https://github.com/KBNLwikimedia/wikimedia-commons_copyright-templates/)
* Story: [Free to use? Exploring public domain claims in Wikimedia Commons files sourced from Delpher](https://kbnlwikimedia.github.io/wikimedia-commons_copyright-templates/stories/Free%20to%20use%20-%20Exploring%20public%20domain%20claims%20in%20Wikimedia%20Commons%20files%20sourced%20from%20Delpher.html) (June 2025)

### [Wikimedia Commons structured data tools](https://github.com/KBNLwikimedia/SDoC)
Code, scripts and stories about dealing with [structured data](https://commons.wikimedia.org/wiki/Commons:Structured_data) for KB files on Wikimedia Commons.

More info about [Structured Data on Commons efforts](https://commons.wikimedia.org/wiki/Commons:Koninklijke_Bibliotheek/SDoC) of the KB.

#### - [Wikimedia Commons category Depicts (P180) extractor](https://github.com/KBNLwikimedia/SDoC/tree/main/wmc-category-depicts-extractor)
Lists all things depicted in all images in a Wikimedia Commons category 
* [Github repo](https://github.com/KBNLwikimedia/SDoC/tree/main/wmc-category-depicts-extractor)

#### - [WriteSDoCfromExcel](https://github.com/KBNLwikimedia/SDoC/tree/main/writeSDoCfromExcel)
Adds Wikidata QIDs to the structured data for one or more properties (e.g., **P180 – depicts**, **P170 – creator**) on Wikimedia Commons files from an Excel sheet.
* [Github repo](https://github.com/KBNLwikimedia/SDoC/tree/main/writeSDoCfromExcel)
* [Tool page on Commons](https://commons.wikimedia.org/wiki/Commons:WriteSDoCfromExcel)

#### - [Delpher-Commons structured data tools](https://github.com/KBNLwikimedia/SDoC/tree/main/delpher-urls-from-wikitext-to-sdc) - TO UPDATE!!
Tools to add, update, improve an manage structured data for [Delpher files on Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Media_from_Delpher)
* [Github repo](https://github.com/KBNLwikimedia/SDoC/tree/main/delpher-urls-from-wikitext-to-sdc)
  - To add: extract-delpher-urls-from-wikitext.py
  - To add: add-delpher-urls-to-sdc.py

#### - [dict2sdc](https://github.com/KBNLwikimedia/SDoC/tree/main/dict2sdc)
Import [structured data](https://commons.wikimedia.org/wiki/Commons:Structured_data) to Wikimedia Commons using [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot). Read data from a dict.csv file and add it as structured data to Wikimedia Commons.
* [Github repo](https://github.com/KBNLwikimedia/SDoC/tree/main/dict2sdc)

## Other Wikimedia tools

### [WikimediaKBURLReplacement](https://kbnlwikimedia.github.io/WikimediaKBURLReplacement/)
Code, scripts and stories about replacing outdated or non-persistent URLs of KB services in Wikipedia, Wikimedia Commons and Wikidata
* [Github repo](https://github.com/KBNLwikimedia/WikimediaKBURLReplacement)
* Story: [Making references to Dutch newspapers in Wikipedia more sustainable](https://kbnlwikimedia.github.io/WikimediaKBURLReplacement/stories/Making%20references%20to%20Dutch%20newspapers%20in%20Wikipedia%20more%20sustainable.html)

### [OpenRefine-Wikibase](https://github.com/KBNLwikimedia/OpenRefine-Wikibase)
Files for interaction between OpenRefine and KB Wikibases, for reconciling and uploading data to Wikibases of the KB, using Openfine 
* [Github repo](https://github.com/KBNLwikimedia/OpenRefine-Wikibase)
* Relevant presentation: [Setting up your own Wikibase reconciliation service (e.g. for OpenRefine)](https://zenodo.org/record/10078805) (Zenodo, november 2023)

### [wikipedia-utilities](https://github.com/KBNLwikimedia/wikipedia-utils)
Utility scripts for working with Wikipedia data dumps 
* [Github repo](https://github.com/KBNLwikimedia/wikipedia-utils)

## Non-Wikimedia tools, but still handy

### TO ADD: [General File Downloader](xxxx)
A simple tool for quickly downloading non-Wikimedia Commons files
* [Github repo](...)

### TO ADD: [URL http status checker](...)
Checks the HTTP status codes of a list of URLs, with support for retries, timeouts, and detailed logging. Works for all URLs, not necessarily Wikimedia-related URLs.
* [Github repo](...)


### [SaveToWaybackMachine](https://github.com/ookgezellig/SaveToWaybackMachine)
Saving URLs of webpages of the KB in bulk to the Wayback Machine of The Internet Archive. Some websites managed by the KB, national library of the Netherlands, have been or will be discontinued. To preserve the content of these sites (e.g. for sourcing Wikipedia articles or cultural heritage preservation purposes) the KB actively submits websites to the The Wayback Machine [web.archive.org](https://web.archive.org/).
* [Github repo](https://github.com/ookgezellig/SaveToWaybackMachine)

### [videotools](https://kbnlresearch.github.io/videotools/) 
A collection of video and audio processing tools. 
* This repo performs various operations on video and audio files, including:
  * Extracting short video clips from longer ones.
  * Enhancing audio by adjusting pitch and volume, eg. for a deeper voice.
  * Compressing and converting video files to WebM format.
  * Extracting audio from a video and saving it as an MP3 file.
  * Amplifying audio if necessary.
  * Transcribing audio using Whisper.
  * Correcting raw audio transcripts using ChatGPT.
  * Embedding subtitles into the WebM video files.

* [Github repo](https://github.com/KBNLresearch/videotools)
* Story: [How to create high-quality offline video transcriptions and subtitles using Whisper and Python](https://kbnlresearch.github.io/videotools/stories/How%20to%20create%20high-quality%20offline%20video%20transcriptions%20and%20subtitles%20using%20Whisper%20and%20Python.html)

