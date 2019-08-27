# LogInBrowser for Sublime Text 3

# An Sublime Text 3 extension for search part of code; using custom search engine.

## HOW TO INSTALL:
Clone or copy this repository into the packages directory. By default, they are located at:
- OS X: ~/Library/Application Support/Sublime Text 3/Packages/
- Windows: %APPDATA%/Roaming/Sublime Text 3/Packages/
- Linux: ~/.config/sublime-text-3/Packages/

## USAGE:
### Log selection:
Select text and go in the LIB thumbnail in the right click's folder and click on "Log the selection". You can also use the 
key binding (for now only on Linux and Windows)
> super+ctrl+l
### Search engine creation and usage:
You can create and modify search engine (SE) using the "Operations on SE" menu. The SE are stocked in the SE_parameters file.
A search engine is composed with an id and a query. The query is an Internet link with the _QUERY_ word after the search request
> https://www.google.fr/search?q=github

become

> https://www.google.fr/search?q=_QUERY_
### Links and SE priority order:
You can link SE with file or extension file using the "Link" menu.
The used search engine (SE) is defined according to a priority order:
- File
- Extension file 
- Default SE
