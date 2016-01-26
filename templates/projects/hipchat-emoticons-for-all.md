# Hipchat Emoticons for All

After starting my new job at Dabapps, I was introduced to the world of [Hipchat](https://hipchat.com), and it's wonderful array of emoticons, as well as the ones added. It was wonderful, it made communicating with friends and colleagues much more interesting!

Unfortunately, the emoticons on the other services we use, like [Github](https://github.com), were terrible in comparison. So it was after a discussion with [@JakeSidSmith](https://github.com/jakesidsmith) about him just using things like (facepalm), (notsureif), and (wat) in [Facebook messenger](https://www.messenger.com/) and hoping people understand what it means, that I decided to make 'Hipchat Emoticons for all', so people like him could use a much better set of emoticons.

The premis is very simple, whenever it sees a hipchat emoticon code, like (notsureif), it replaces it with an emoticon. If only writing the code could have been this simple! I started writing the plugin in firefox, using [Jetpack](https://wiki.mozilla.org/Jetpack), which uses Javascript. The initial stages of the code were very simple, but I encountered problems making sure that anything loaded after the page was loaded (such as a facebook message), be changed too.

Fortunately after many hours of testing, and changing the code, I finally got everything working perfectly, and in a way that made adding new sites incredibly easy! The code isn't the greatest in terms of performance, and there are some things that could have obviously been done better, but this was all done to help with a shared codebase between Chrome and Firefox, which don't play nice when it comes to extensions.

Currently the application is in very beta stages right now, only having tested partial support for github, but the code is all available on GitHub, if people have their own suggestions of improvements.

#### Links coming soon
