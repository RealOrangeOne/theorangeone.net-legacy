---
title: Cyber Security Month 2016
date: 2016-10-01
template: blog
summary: The best time to upgrade the security on my projects!
---

As it's [Cyber Security Month](https://cybersecuritymonth.eu/), now's the perfect time to work on improving the security on my websites, projects, and servers. But, upgrading them for now isn't good enough for me, I want to add a way of scanning projects automatically during unit tests, to check for any new vulnerabilities.

As most of my projects revolve around NodeJS and Python, these are the languages I'll be concentrating on.

## Express Server
Express is one the most popular JS servers, and fortunately, they have a [security guide](http://expressjs.com/en/advanced/best-practice-security.html), that contains some of best ways to write secure servers. One of the best and simplest ways is to add the [helmet](https://www.npmjs.com/package/helmet) middleware, which contains various other middleware that drastically increase security. It's incredibly easy to add too, at just 3 lines of change, [like this](https://github.com/RealOrangeOne/host-container/commit/90adfd04aed2f2065d803623c297dc1a8ae71632)!

You can use [securityheaders.io](http://securityheaders.io/) to check if any headers are being sent by your server that shouldn't be, As well as see how you can improve.

## NodeJS Dependencies
One of the easiest ways to keep secure is make sure your dependencies are secure. If your code is secure, but one of your dependencies isn't, it's a waste! Fortunately there's a tool to check this, [nsp](https://www.npmjs.com/package/nsp). It checks the [Node Security Project](https://nodesecurity.io/) for known vulnerabilities in your dependencies, and reports them.

If you don't want to add `nsp` to your dependencies, they offer a [CI service for GitHub](https://nodesecurity.io/#pricing) which will run the checks for you on their own servers.

### Checking for updates
Keeping dependencies up to date is generally a good thing, and likely to help with the above. Upload you `package.json` to [npm.click](http://npm.click/), and it'll tell you what's out of date, and what the most recent version is!

## Python Code
Any of the projects I work on that are more advance that a simple static server, are probably Django, written in Python. Checking the python code itself is nice and simple thanks to [bandit](https://github.com/openstack/bandit). It checks your code to make sure you're writing it properly, and are catching errors.

### Dependencies?
As with NodeJS, there's a tool that checks dependencies for security issues. But, unlike `nsp`, [safety](https://pypi.python.org/pypi/safety) not only checks your dependencies, but also their dependencies.

It's also possible to check for updates using [pypiup](https://pypi.python.org/pypi/pypiup/). Working in much the same way as npm.click (and written by the same person), except it's a CLI rather than a website.

## Checking
To check your hard work has made a difference, [seositecheckup](http://seositecheckup.com/) contains a helpful section on security, as well as the previously mentioned [securityheaders.io](http://securityheaders.io/). I've enabled these tricks on my website, and you can see their results here for [securityheaders.io](https://securityheaders.io/?q=https%3A%2F%2Ftheorangeone.net&followRedirects=on) and [seositecheckup](http://seositecheckup.com/seo-audit/theorangeone.net).
