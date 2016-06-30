title: LanSchool
slug: lanschool

LanSchool is the software of choice for my college to monitor and control computer usage. It allows teachers to see students screens, interact with them, and even block certain functionality like the internet and removable storage. My secondary school had a system much like this, but they weren't as active in using it.

By far the worst feature of LanSchool was the screen blocking. At will, a teacher could show an overlay on your screen, usually consisting of test saying _"Eyes front"_ etc. The problem with this pop up was there was no way to hide it, it just appeared suddenly and forced you to stop using your computer. This tool had to be stopped!

Within a few weeks of realising this tool, A friend of mine discovered how to get around it in a really primitive way: simply unplugging the ethernet. It's rather incredible this worked, but it had some problems:

- It took around 10 seconds after disconnect before the screen was restored, not a major problem, but still annoying.
- With all documents and programs bring stored on the network, you couldnt access any programs and documents you didn't already have open.
- When you reconnect the cable, the screen returns to the state of everyone else.
- Your computer would suddenly dissapear from the list of machines on the teachers screen. If they were observant, they'd notice!

This solution worked, but wasnt ideal. Another solution was to log out (using the `ctrl + alt + delete` shortcut, which worked for some reason), and log in again. Our network was slow, so sometimes it wasnt worth the wait if your screens were only disabled for a short period of time. However the main problem with this was the fact it didnt always work, only around 30% of the time.

#### The best fix

The original idea for this came from someone else, but the implementation and refinement was mine, so I like to think it was mostly me.

Using an ubuntu live CD loaded onto a USB drive, we booted to ubuntu, and renamed the LanSchool executable. This meant the program wouldn't be able to run on start up, and so the client couldnt communicate with the teacher to lock our computers. __Result!__

This method worked almost perfectly, however had a few problems:
- It took at least 10 minutes to go from completely enabled, to completely disabled
- It worked for every user account on that computer, so it had to be done on each computer I used.
- A teacher would notice, as you would never show up on their list.

Fortunatley this last point is a non-issue, as usually the teachers put it down to the software messing up, not a student breaking the install. Another key problem with this is that it's rather obvious when everyones computer other than yours is disabled, as youre still actively using yours, whilst everyone else is actually listening!

#### The silver lining

Disabling the client on a machine also allowed for another feature that I had never thought of, but was by far the greatest bi-product of disabling LanSchool: __Teacher Mode!__

Due to me being able to have access to a teachers computer one evening, I was able to copy the executables for the teachers console onto a USB drive, and then run them later on my computer. Obviosuly I know most software won't work in this way, but i'm so glad this one did!

Now, I had access to everything the teacher did, which made lessons much more exciting. I could block peoples screens, send them messages, or even take complete control of their computer, it was great! Eventually a few more in my class knew [I had the power](), and I became a tool for trolling people, which was made extra simple by the fact I had access to all student computers in the college, not just my class. The only downside to this (something I didnt realise until I tried to prank a friend), is that it comes up with your name on the client computer if you try and take control of one that's not in your class, an annoying and dangereous feature.

#### Phase 2

Whilst writing this article, over 2 years after all this, I realised I could improve it considerable. Writing some kind of wrapper program, to detect my username, and run LanSchool for users other than me, would be harder to work out there was a problem with the computer, as well as prevent it disabling LanSchool for every user.
