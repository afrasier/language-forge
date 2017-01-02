# language-forge
Create fantasy languages for use in RPGs and Videogames

python 3 for unicode fun

Want to contribute? Create an issue so I know what you're working on and then make a PR when you're done!

# TO-do
Handle contractions
Add a few more example languages
Add api front end

# How it works
Language forge uses a set of rules defined in a language class (for example, `high_common.py`). These rules consist of an array of tuples with which to encode the English, and optionally, an override of the syntax parsing allowing users to restructure a sentence based on part of speech tagging. Additionally, it is possible to "strip" different parts of speech using an array of tags. See comments for more info

# How to set-up
* Use Python 3, as unicode plays nicely with it as compared to Python 2
* `pip install -r requirements.txt` to install required libraries
* `python language-forge.py -i` to install nltk corpora

# How to use
```
Usage: language-forge.py [options] sentence

Options:
  -h, --help            show this help message and exit
  -t, --test
  -l LANG, --language=LANG
                        Language which to translate the given string. Options:
                        base, high_common
  -f FLUENCY, --fluency=FLUENCY
                        Listener's fluency with the language
  -i, --install-corpora
                        Install ntlk corpora
```

* `FLUENCY` goes from 0.0 to 1.0.
* Specify multiple languages by specifying `-l` mutliple times. NB: They will share whatever the fluency value is

# Piping in a file
Yep, you can do that.

```
$ cat astley | python language-forge.py -l high_common


Using language: High Common with 0.0 fluency

English                                            -->  High Common
#######################################
We are no strangers to love                        -->  Hist erhi aifo srheaifhuirhs to ylof
You know the rules and so do I                     -->  Ëist uchaifoh tchi rheylis eaifd so tun Ëist
A full commitment is what I am thinking of         -->  E feyl uchokhmëtmiaift ës chet Ëist em tchëaifuchëaifhu of
You would not get this from any other guy          -->  Ëist hoeyld aifot huaí tchës frhom eaifë otchirh huë
I just want to tell you how I am feeling           -->  Ëist ües heaift to tiyl ëist choh Ëist em fëylëaifhu
Gotta make you understand                          -->  Huot te meuchi ëist eaifdirhseaifd
Never gonna give you up, never gonna let you down  -->  Aififrh huoaif aife huëf ëist e, aififrh huoaif aife ylaí ëist tunhaif
Never gonna run around and desert you              -->  Aififrh huoaif aife rheaif erhoeaifd eaifd disrht ëist
Never gonna make you cry, never gonna say goodbye  -->  Aififrh huoaif aife meuchi ëist uchrhë, aififrh huoaif aife saí huuchdbëi
Never gonna tell a lie and hurt you                -->  Aififrh huoaif aife tiyl e yle eaifd cherht ëist
```

# Example output

```
Using language: Base with 0.0 fluency

English                                 -->  Base
#######################################
she gave him the ball                   -->  she gave him the ball
testing a test sentence for testing     -->  testing a test sentence for testing
Hello, traveller!                       -->  Hello, traveller!
Would you like to buy some goods?       -->  Would you like to buy some goods?
Attack!                                 -->  Attack!
Farewell for now.                       -->  Farewell for now.
I suppose... if that is what you want.  -->  I suppose... if that is what you want.
Whew! I am a bit stressed now.          -->  Whew! I am a bit stressed now.
I would rather not do that, Julian.     -->  I would rather not do that, Julian.


Using language: High Common with 0.0 fluency

English                                 -->  High Common
#######################################
she gave him the ball                   -->  sist huef cist tchi beyl
testing a test sentence for testing     -->  tisëaifhu e tis saiftiaifuchi uchrh tisëaifhu
Hello, traveller!                       -->  Chiylo, trhefylirh!
Would you like to buy some goods?       -->  Hoeyld ëist ylëuchi to beë somi huuchds?
Attack!                                 -->  E'euch!
Farewell for now.                       -->  Ferhihiyl uchrh aifoh.
I suppose... if that is what you want.  -->  Ëist seos... ëf tchet ës chet ëist heaift.
Whew! I am a bit stressed now.          -->  Chih! Ëist em e bët srhisset aifoh.
I would rather not do that, Julian.     -->  Ëist hoeyld rhetchirh aifot tun tchet, Üeylëeaif.


Using language: High Common with 0.5 fluency

English                                 -->  High Common
#######################################
she gave him the ball                   -->  she huef cist the beyl
testing a test sentence for testing     -->  tisëaifhu a tis saiftiaifuchi for testing
Hello, traveller!                       -->  Hello, traveller!
Would you like to buy some goods?       -->  Hoeyld you like to buy some goods?
Attack!                                 -->  E'euch!
Farewell for now.                       -->  Farewell for aifoh.
I suppose... if that is what you want.  -->  I seos... if that is chet ëist heaift.
Whew! I am a bit stressed now.          -->  Whew! Ëist am a bit srhisset aifoh.
I would rather not do that, Julian.     -->  I hoeyld rather aifot do tchet, Julian.


Using language: High Common with 0.9 fluency

English                                 -->  High Common
#######################################
she gave him the ball                   -->  she gave him the ball
testing a test sentence for testing     -->  testing a test sentence for tisëaifhu
Hello, traveller!                       -->  Hello, traveller!
Would you like to buy some goods?       -->  Would you like to buy some goods?
Attack!                                 -->  Attack!
Farewell for now.                       -->  Farewell for now.
I suppose... if that is what you want.  -->  I suppose... if that is what you want.
Whew! I am a bit stressed now.          -->  Whew! I am a bit stressed now.
I would rather not do that, Julian.     -->  I would rather not do that, Julian.


Using language: High Common with 1.0 fluency

English                                 -->  High Common
#######################################
she gave him the ball                   -->  she gave him the ball
testing a test sentence for testing     -->  testing a test sentence for testing
Hello, traveller!                       -->  Hello, traveller!
Would you like to buy some goods?       -->  Would you like to buy some goods?
Attack!                                 -->  Attack!
Farewell for now.                       -->  Farewell for now.
I suppose... if that is what you want.  -->  I suppose... if that is what you want.
Whew! I am a bit stressed now.          -->  Whew! I am a bit stressed now.
I would rather not do that, Julian.     -->  I would rather not do that, Julian.
```
