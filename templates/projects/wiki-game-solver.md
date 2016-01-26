# Wiki Game Solver

For those who dont know what the Wiki Game is: [The Wiki Game](http://thewikigame.com) is an online game where you attempt to navigate through wikipedia from a start page to a goal page using as few other pages as possible. Once i was shown the Wiki Game by my friend, and after i realised that I really wasn't very good at it, I looked into how the system worked, and how I could beat it.

I couldnt see how the back end worked, but after playing a few games and checking what happened on the page,the way that the game was won was when the iframe was at the final page location, or at least a clone of it on their servers with extra querystring information.

With this information, I started to write some javascript that would change the location of the iframe to the goal. Fortunately for me, there was already a link to the real winning page, so I could use that to construct the final URL, and direct the iframe to it, meaning I was able to win the game in 1 turn.

## Source
Naturally, the source for this was written in javascript, and relies heavily on the fact that the wiki game uses jQuery so I can plug into components and events really easily. The code can be found in the GitHub gists below. Both the standard and compact versions are available.

<script src="https://gist.github.com/RealOrangeOne/7da9a3dd1bf90ecdf7be.js"></script>

## Usage

1.  Start a new game on [Wiki Game](http://thewikigame.com/speed-race), __don't__ press start!
2.  Open your browser's developers console. This will vary from browser.
3.  Open the Javascript console
4.  Paste the compact version of the code there, and execute it (press enter)
5.  Congratulations, you just won!

If you want to win more games, just re-paste the code, it works as often as you like!

### Disclamier

As I experienced whilst developing this, the people that play Wiki Game don't tend to like people cheating. There were a lot of people getting very annoyed whilst I was developing and testing. So please use this at your own risk! At the moment I don't think there is any kind of banning system, but be warned!
