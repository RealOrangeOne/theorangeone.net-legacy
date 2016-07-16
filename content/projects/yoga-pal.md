title: Yoga Pal
template: projects
slug: yoga-pal
repo: https://github.com/RealOrangeOne/yoga-pal
summary: Control screen rotation, touch screen, and trackpad using the terminal

Once I started work, I bought myself a _Lenovo Yoga 3 14"_ laptop, because I needed a thin and light for trains etc. Unfortunately this came with windows, which within 10 minutes was running Ubuntu Gnome! Ubuntu greatly increased the performance, but I had to sacrifice all the screen, touchpad and keyboard customisation when changing 'modes'.

I found [this thread](askubuntu.com/questions/450066/rotate-touchscreen-and-disable-the-touchpad-on-yoga-2-pro-in-rotated-mode) on _Ask Ubuntu_ with someone else trying to find a solution to this, to find a nice way of rotating the screen when in tablet mode. On the thread was a really nice simple [script](http://askubuntu.com/a/485685/432138) that rotated the screen perfectly, and did the touchscreen too. This script worked great, doing exactly what it said it did, nicely and quickly, however it wasn't a great solution for me. Yes it worked, but it didn't allow me to change anything else, like the touchpad.

So I started working on my own CLI, based off the above script, to allow me to tweak everything, so the laptop can be used as it was intended.
