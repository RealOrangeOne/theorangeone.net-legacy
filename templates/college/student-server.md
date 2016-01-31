# Student Server
Back when I was in college, we needed a server for computing students to learn how to FTP, and script on a server using python CGI and <a href="Link to tonys php toolbox analagy">PHP</a>, as well as possibly for some students coursework. Fortunately, the college already had one, running the IT students microsite for extra course information. The problem was that it was majorly out of date, and no one really new how to use it properly. It was up to me and my friend Alex to bring the server up to date, and make it ready for the students who needed it.

The original plan was to update the server's OS (at that stage running Ubuntu 12.04 LTS), install python and PHP backends, add student users, and then make sure they couldn't edit eachothers documents. In the end Alex did a server backup, and then fully reinstalled the server OS from scratch, and then pushed the documents back on, which made our lives a lot easier.

Because he had worked with servers a lot in the past, and was already very fluent with the ubuntu terminal, he installed the software that was needed, and got it all configured properly, whilst I worked on the student logins and permission structure.

## User Creation

I knew we would need user accounts for the computing teachers, for the students doing A2 computing, and for updating the IT site, but I wasnt expecting this to amount to over 50 user accounts that needed to be created, and permissions setup for their accounts. It was then that I realied that I would need to write a script to do this in any useful amount of time. Fortunately Alex had started writing one with a small amount of logic, so I had something to work off to get this done, as this was my first major linux project.

The basis of the script was to load information about the users from a database I had created with all the required students in, create users based on this information, and configure the permissions for their user and their home directory. The script also allowed for manual entering of users with the same permission template, in case single users needed to be created. An additional feature that I added which has proved useful now that i've left is the ability to delete users manually, and from that original database, to make sure that no student will have access to the server once they have left, well, other than me that is!

The script I used to create these files can be found below, hosted as a gist on github. Unfortunately some of the information has been redacted to prevent giving too much information that could be considered a security threat to the server. The script may not work in this redacted state, however all the core logic has been kept.
