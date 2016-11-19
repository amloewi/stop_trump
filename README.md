# Stop Trump

However you want to do it, this is a script that makes it a little easier. With very little work, it will send emails to
 electoral college voters with public emails, OR, to a massive list of journalists, editors, and newspaper owners (again,
 whose emails are public). Journalists, surprise surprise, get written to much less, and are much more likely to see what you send.
 ALTHOUGH, in every case, a phone call is still more powerful than email.

I tried to make this a website, but the value here is that the email the recipienct see will be from YOUR ACCOUNT,
not from a million-person petition, and that makes gmail permissions a lot trickier. For now, there's this.

## How To:

Do you have a gmail account? Can you open a Terminal? No? Well sign up for one, Google "Open a terminal Mac" And you're ready to go. Now:

###1) Download this code
Click on the green 'Clone or download' button in the upper-right corner of this page. Click on "Download ZIP."

###2) Edit this code
Double-click on the file that gets downloaded, and open "stop_trump.py". You can use any text editor the computer suggests.
Follow the instructions in the file, which are mostly about what to put in what place (name, subject, email, etc.). Don't touch
anything else!

###3) Run this code
Open a Terminal. 'cd' to the place where "stop_trump.py" is, meaning if the file is in `/Users/alexloewi/Desktop/stop_trump`,
then type `cd /Users/alexloewi/Desktop/stop_trump`.

Type `sudo easy_install yagmail` (and enter your password for the computer if it asks you to).

Type `python stop_trump.py electors`

OR

Type `python stop_trump.py newspapers`

And you've done it -- on to the next act.


