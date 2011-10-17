===================================
How to Moderate an inSCIght Episode
===================================
Congratulations!  You have been selected to moderate an inSCIght episode.
This lofty task puts *you* as the front-facing representative of inSCIght.
The only requirement for being a moderator is that you must have previously
been a panelist on the show once.

You have been chosen for this task by this episode's organizer.  Or, more
likely, you are the show's organizer as well.

You duties as moderator also are extended to those of editor as well.
Here is a quick list of what you'll need to do:

    #. Set up your recording environment
    #. Last minute recording test
    #. Pre-Game with panelists
    #. Record the show
    #. Post-Game with panelists
    #. Edit the show
    #. Upload the show
    #. Post to the blog
    #. Profit

Note: Once you have done this once or twice, it becomes second nature.

---------------
Recording Setup
---------------
In addition to running the show, you are also responsible for 
recording the show.  You are welcome to do this in any way that 
you want.  However, typically we have people call into a conference 
call on skype.  There are a plethora of skype recording software out 
there.  A free one that works on Linux is called "skype-call-recorder".

Make sure that your recording setup works prior to the show.  
The sooner the better.  If you have never recorded a show before
test that your system records call *at least* a day in advance.
Then, about a half an hour before the show, check and make 
sure that you can record calls.

Skype provides an 'Echo Test' system that you can call into and
verify that your call recording software is working.


-------------------
Show Test Recording
-------------------
When the designated recording time comes, you'll need to initiate a
conference call once all of the panelists are online.  (Note: you cannot
initiate a conference call from mobile devices.)

Once you have everyone on the call and talking and recorded for a couple of 
seconds, you'll have to verify that your recording actually works!  
(I know that this is a lot of tests, but it is worth it.  Trust me.)
Tell everyone something along the line of the following:

    OK everybody.  I am going to kill this call, make sure I can hear 
    everyone on the recording, and then call everybody right back.  Cool?
  
Then as you just stated,

    #. Kill the call
    #. Fire up an audio player
    #. Verify that you can hear everyone on the test recoding
    #. Call everybody back.


--------
Pre-Game
--------
Now that you have everybody on a conference call that you are recording, you can go 
ahead with the pre-game.  The pre-game takes between 10-20 minutes before you start 
the actual show.  This should be recorded as well.  (In fact from here on, don't
stop recording.)

The first thing to do is (together with your organizer) to introduce the panelists
to each other.  

Then, you get to introduce the topic to the panelists.

Next, and very importantly,  you need to explain how the recording works to the 
other panelists.  Say something like:

    *"So this is going to work is that right now we'll have about 10-20 minutes
    for us to talk about what we are going to talk about on the actual show.
    This will help us become more comfortable with each other.

    Then when I think we are good to go (we want to get out of here on time), 
    I'll let everyone know that I am starting 5 seconds of silence before we 
    record the actual show.

    After the 5 sec of silence, I'll dive right into reading the intro blurb, 
    introducing you all.  Then I'll kick it off to {panelist} to introduce
    this week's topic.  

    While this is a panel discussion, I like it to be more like a conversation
    and less strictly formal.  Therefore during the actual show, if you hear 
    something that you object to or have a comment, feel free to jump right in
    and say something, or laugh, etc.  Especially if the other person has been 
    speaking for 30 seconds or a minute.  Do not worry about moderating.  That 
    is my job.  If someone oversteps their bounds, I'll step in.  Please
    be collegial!

    After the bulk of the show, I'll transition into our rant section.  So be 
    prepared to spend 15 - 30 secs on your soapbox.  

    After rants, I'll read the outro blurb.  Then we'll have 5 seconds of 
    silence and then we can sit and chat for a little while afterward, if
    you want.

    Sound good to everyone?  

    I figured we could start the discussion from some of the points mentioned
    on convore..."*

Then you'll need to do exactly what you just said.  Spur the discussion along
for 15 +/- 5 minutes, being mindful of the time.  Then call 5 sec of silence.
This marks the end of the pre-game!


-------------------
Recording the Show
-------------------
After the five seconds of silence, you are in the real show.  Here is what you 
need to do:

    #. Read the `intro blurb`_
    #. Substitute the panelist's `short biographies`_ into the intro blurb
    #. Do a 1 sentence introduction of today's topic
    #. Kickoff to a panelist of choice to do a more lengthy topic introduction
    #. Keep the conversation moving from here (20-40 mins)
    #. Transition into rants
    #. Do your rant last
    #. Read the `outro blurb`_

Typically, you should record the show for 30 - 45 minutes.  After editing, this time will
be reduced.


---------
Post-Game
---------
Give everyone a hardy thanks for doing the show.  Continue the conversation, if appropriate.


----------------
Editing the Show
----------------
(Warning: this part takes a couple of hours!)

One of your duties as a moderator is to edit the raw episode that you have just recorded.
There is a variety of audio editing software out there.  One that I like that is 
cross-platform is called "audacity".  

If the skype conference call was recorded as a multi-track AAC file, the tracks
can be split for importing into audacity with ffmpeg::

  ffmpeg -i input.aac -map 0:0 output0.wav

This will save the first track.  The option `-map 0:1` will extract the second
stream.

The following is the editing work flow that I have found that works best:

    #. Load the show into a new project.
    #. Cut the pre-game and post-game parts of the show out.
    #. Line the fade-out of the intro music up with the 
       show's intro blurb.
    #. **Important:** Listen to the whole show, removing
       silent periods over 0.5 sec and extraneous "Ummm"s and 
       "Like"s.  This part takes a while, but is critical.
    #. Run Effect -> Leveller... on the whole project to balance difference
       voice levels.
    #. Run Effect -> Normalize... on the whole project to get the overall volume correct.
    #. Optionally run Effect -> Noise Removal... and Effect -> Plugins 1 to 10
       -> High Pass Filter... to clean up the audio.
    #. Import the intro/outro music in another track.  Tracks -> Add new ->
       Stereo Track.
    #. Find a 5-15 sec intro music clip and place it at t=0.
    #. Fade the intro music in and out.
    #. Place the speech at the right location in the timeline.  More dead time
       can be added with Generate -> Silence...
    #. Find another 5-15 sec to use as the outro music.  
    #. Fade the outro music in an out.
    #. Line the outro music fade in up with the end of the 
       show's outro blurb.
    #. Export as an mp3.  Use the Audacity `tags template`_.
       Use the naming convention: "inscight_{num}_{year}_{month}_{day}.mp3".

This seems like a lot work, but it is what turns our podcast from "pretty good" to 
"quality".  Said another way, we don't want potential listeners walking away from the 
show because they didn't like the audio quality.  People will ignore your ideas if 
they are not in an easily digestible format.  Treat every episode like it is the
first episode that someone might hear.

I would love it if we could pay to have someone do this for us.  I have priced it 
at about $1000 per year (~$20 per episode).   Ideas for funding are always welcome.


------------------
Uploading the Show
------------------
Right now, we have hosting via Enthought.  So you need to get the mp3 to 
scopz (Anthony Scopatz).  More publicly available suggestions are welcome!


------------
Post to Blog
------------
Whew!  After all that hard work, you finally get to let the world know about your 
super-awesome episode.  Please copy the `blog template`_ into a new post over 
at the `inSCIght blog`_ (wordpress.com).  (Note that you need to copy it into
'HTML' mode rather than 'Visual'.)  To get administrator access to the WordPress
account, send Anthony your WordPress account email.

Now you just need to fill the template out!  Keep in mind that if you both moderated 
and organized this episode, only give yourself the much cooler 'moderator' credit.
If the organizer was not actually on the show, please note that they organized the show
somewhere in the main body.  

At last, you are good to go.  Hit that publish button like it has never been hit before!

(Also, if someone on the show does not have their bio on either the 'Bio' or 'Guests'
page, please add it now).

Additonally, we are also part of the network over at `Science Podcasters`_.  All
you have to do, is copy-paste that post you just wrote for our own website and
make a post over there. Sign in as ``inSCIght``.  The password can be obtained
from Anthony or Matt.  Be sure to put the post in the ``inSCIght`` category so
it becomes linked to our show.

We should really have a tool that posts out to all of these websites... 


------
Credit
------
Congratulations!  You now have the enduring gratitude of inSCIght devs and listeners
everywhere, in all time.


.. _intro blurb: https://github.com/inscight/inscight/blob/master/docs/intro_blurb.rst

.. _short biographies: https://github.com/inscight/inscight/tree/master/docs/bio

.. _outro blurb: https://github.com/inscight/inscight/blob/master/docs/outro_blurb.rst

.. _tags template: https://github.com/inscight/inscight/raw/master/src/show/inscight_audacity_tags_template.xml

.. _blog template: https://github.com/inscight/inscight/blob/master/docs/blog/episode_post.html

.. _inSCIght blog: http://inscight.org/

.. _Science Podcasters: http://www.sciencepodcasters.org/

