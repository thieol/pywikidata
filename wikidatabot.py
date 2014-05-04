import wikidata
import errors 

class wikidatabot(object):

    """This is a helper class to use in bots. Somm cheks are done before updates."""

    def __init__(self):
       self.lang = None

    def set_lang(self, lang):
       """gets the language in which you want to work."""
       self.lang = lang 

    def get_lang(self):
       """sets the language in which you want to work."""
       return self.lang

    def getItem(self, id):
       """gets an item by its id ( number or beginning with q."""
       item = wikidata.api.getItemById(id)
       if ( str(item.id)[0:1].lower() == "q" ):
          item.id = str(item.id)[1:]
       return wikidata.api.getItemById(id)

    def updateDescription(self, id, lib, comment="", force=False):
       """update description. if description exists, nothing is done instead force=True
          when updating a comment is adding.
       """
       item = wikidata.api.getItemById(id)
       if self.lang in item.descriptions:
          if len(item.descriptions[self.lang]) > 0:
             if not force : 
                raise errors.InvalidBotOperation("description is not tempty")  
       if ( str(item.id)[0:1].lower() == "q" ):
             item.id = str(item.id)[1:]
       item.descriptions[self.lang] = lib
       sumary = comment + "Bot adding ["  + self.lang + "] description ->" + lib
       wikidata.api.save(item, sumary)


    def updateLabel(self, id, lib, comment="", force=False):
       """update label. if label exists, nothing is done instead force=True.
          when updating a comment is adding.
       """
       item = wikidata.api.getItemById(id)
       if self.lang in item.labels:
          if len(item.labels[self.lang]) > 0:
             if not force :
                raise errors.InvalidBotOperation("label is not tempty")  
       if ( str(item.id)[0:1].lower() == "q" ):
             item.id = str(item.id)[1:]
       item.labels[self.lang] = lib
       sumary = comment + "Bot adding ["  + self.lang + "] description ->" + lib
       wikidata.api.save(item, sumary)

