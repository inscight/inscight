Notes for Setting Up skype-call-recorder on Mac Hardware in Linux
=================================================================
There are a couple of different issues here.  First is running the programs
and second is configuring the system. 

Running
-------

    * Run skype-call-recorder (v0.8 or higher)
    * Run skype itself.


Configuration
-------------

The default device on skype is not pointed to the correct place.
Instead,  

    * Go to ``Options -> Sound Devices -> Microphone``,
    * Point this device to the third option down, or the one that reads
      ``HDA Intel, Cirrus Analog Default Audio Device (default:Card=Intel)``, 
    * Hit apply, 

and you should be good to go.

ALSA itself also needs to be properly configured to get the best sound.
In gnome-alsamixer, make sure the mixed levels are as follows::


      Line      Mic    Capture   Digital   Internal

      100      50-80     100      100        0

    Rec [ ]            Rec [x]             Rec [ ]

    -----------------------------------------------

    [ ] Surround Speaker
    [x] IEC 958
    [x] IEC 958 Default PCM
    [ ] Rear Mic

Other configurations *may* work, but this one is known to.
