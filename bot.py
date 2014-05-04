from wikidatabot import wikidatabot 

if __name__ == "__main__":
#-------------------------
  
    lang = "fr"
    id = "Q1247955"
    bot = wikidatabot()
    bot.set_lang("fr")
    item = bot.getItem(id)
    if lang in item.labels:
       print item.labels[lang]
    bot.updateLabel(id , "Kathleen Lockhart Manning")
    bot.updateDescription(id , u"compositrice am\u00E9ricaine")
    
