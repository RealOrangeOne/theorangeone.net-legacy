title: BSOD Enabler
template: projects
slug: bsod-enabler

For those that use Windows, the famous [Blue Screen of Death](https://en.wikipedia.org/wiki/Blue_Screen_of_Death) is an annoyance that plagues computers, causing error, frustration, and even data loss. They happened to me a lot whilst I was trying to configure my computer, and I thought _I wonder who else I can annoy with a BSOD_

__And thus the BSOD_Enabler was born!__

After researching into it for a while, it turns out that there are a few different ways to cause a BSOD, unfortunately most of which are by doing things that are meant to cause a BSOD, and can therefore be dangerous to a computer, something I didn't really want. Then I stumbled upon [this article](http://www.wikihow.com/Force-a-Blue-Screen-in-Windows), which shows that you can in fact raise a BSOD without causing any errors or damage to your computer. Now to write a program that can do it too!

Obviously there are many different ways, and probably far better ways of doing this, but I wanted something that was simple to use, fast, and could be done by anyone, no matter how technically illiterate. So I decided to write it in C#, and use a windows console interface.
