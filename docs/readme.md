# MTG Tools

This library has some tools that attempt to aid in making some statistical models for the card game Magic the Gathering.   The goal of the library is to be able to mimic the actions needed to play a game of Magic the Gathering; i.e. draw cards, get a card from deck, shuffle deck, place cards in graveyard, etc.  The question it is trying to answer is [[Standard] What is the chance to hit delirium off of a single Vessel of Nascency with an empty graveyard?](https://www.reddit.com/r/spikes/comments/5eaf7r/standard_what_is_the_chance_to_hit_delirium_off/).  The answer to this is about 66% of the time and this model also gets the same answer. 

**Usage**
See the example in delirium.py for usage.

**Prerequisites**

[mtg sdk python](https://github.com/MagicTheGathering/mtg-sdk-python) this can be installed by running:
    `pip install mtgsdk`

**Authors**

John Barksdale
