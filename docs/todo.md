# Todo:
* James requested to find out how often you will get a hand of two castable creatures, a discard outlet and 2 vengevines by turn 3 (with 2 lands)
* Figure out way to handle double cards
    * If you look up Claim then in names is Fame
* ~~Figure out how to use optional named keywords in class constructor~~ 2017/08/01 JB
* ~~Figure out way to mock the Card class or create own that is compatible with the one from mtgsdk so that you don't have to do an API call all the time.~~ 2017/07/31 JB
* ~~Figure out why some tests fail when all tests are ran at once but when you isolate the tests to their own test class or unnittest they all pass~~ 2017/07/31 JB
    * ~~I think it has something to do with either namespace confilcts or with where the class objects are being created (IE myhand = Hand())~~ 2017/07/31 JB
* ~~In get_card change it so that the card name is wrapped in double quotes~~ 2017/07/31 JB
* ~~On deck import load all the cards as a mtgsdk card object so that the model will run faster.  Original run of program took 19321 seconds or 5.3 hours.~~ 2017/07/30 JB
* ~~Original program returned 100% chance to hit delirium.  This is false.~~ 2017/07/30 JB
    * ~~Reset delirium flag on each run~~ 2017/07/30 JB
    * ~~Return land and swamp from battlefield to library~~ 2017/07/30 JB
    * ~~Check to ensure deck size is the same as imported list before doing another loop~~ 2017/07/30 JB
* ~~Add a requirements.txt file~~ 2017/07/30 JB
