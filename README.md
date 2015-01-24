Django-gruyere
=============
Things you should never do when building django projects.

Why this?
=============
It would be nice to have an insecure app to test some common attacks like SQL injection or XSS.
This would help:
* understand how those attacks work
* how to write secure stuff
* like the universe of things django does for you
* have fun build your own attack vectors

Writing this app, I noticed in the meanwhile that build an insecure django app is quite
"hard". It's not impossible of course, but I think you must put a lot of effort to do
such a thing.

Requirements
============
* PostgreSQL 9.3

Installation
============
After you have PostgreSQL installed run `make bootstrap` (you're on windows? LOL), this will create
a virtualenv inside your folder, activate it an  download all dependecies from `requirements.txt`,
finally the local server will start.