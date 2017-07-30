# Todo:
* On deck import load all the cards as a mtgsdk card object so that the model will run faster.  Original run of program took 19321 seconds or 5.3 hours.
* Original program returned 100% chance to hit delirium.  This is false.
    * Reset delirium flag on each run
    * Return land and swamp from battlefield to library
    * Check to ensure deck size is the same as imported list before doing another loop

# Bugs:
* Found a bug in gatherer.  When I search for Murder by name it does not return murder.  Changed Murder to Lightning Bolts for my test model because they are both instants.