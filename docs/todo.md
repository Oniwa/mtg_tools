# Todo:
* Figure out way to handle double cards
    * If you look up Claim then in names is Fame
* Figure out way to mock the Card class or create own that is compatible with the one from mtgsdk so that you don't have to do an API call all the time.
* ~~Figure out why some tests fail when all tests are ran at once but when you isolate the tests to their own test class or unnittest they all pass~~ 2017/07/30 JB
    * ~~I think it has something to do with either namespace confilcts or with where the class objects are being created (IE myhand = Hand())~~ 2017/07/30 JB
* ~~In get_card change it so that the card name is wrapped in double quotes~~ 2017/07/31 JB
* ~~On deck import load all the cards as a mtgsdk card object so that the model will run faster.  Original run of program took 19321 seconds or 5.3 hours.~~ 2017/07/30 JB
* ~~Original program returned 100% chance to hit delirium.  This is false.~~ 2017/07/30 JB
    * ~~Reset delirium flag on each run~~ 2017/07/30 JB
    * ~~Return land and swamp from battlefield to library~~ 2017/07/30 JB
    * ~~Check to ensure deck size is the same as imported list before doing another loop~~ 2017/07/30 JB
* ~~Add a requirements.txt file~~ 2017/07/30 JB

# Bugs:
* Found a bug in gatherer.  When I search for Murder by name it does not return murder.  Changed Murder to Lightning Bolts for my test model because they are both instants.
    * To return the card Murder surround the text with double quotes ("")