# About my website
My website is the culmination of all my knowledge, compiled into 1 place. It not only contains all my projects, but it in itself is a project. Making sure this website works properly is a tall order, especially considering it's self hosted.

## The Website
The website itself is written in python, using the Django framework, and a SQLite database. For what I need it's more than overkill, but hey, why not!

I went with the Django framework because it's what I use with at work, as well as the fact it's simple, clean and easy. It also allows for some server side assets, eg blogging.

The only reason I have a database is because certain sections require it. For this reason I went with SQLite, because it's really lightweight and simple.

## The server
The website is hosted on my UK VPS. Previous versions have been hosted on 1&1 and MyWindowsHosting.

The Django application itself is served using waitress. This get's it's port from a custom reverse proxy allowing me to host multiple sites on a single server easily. This is the same one I use for local development. The main web-facing server is nginx, because it's simple to setup, and damn fast!
