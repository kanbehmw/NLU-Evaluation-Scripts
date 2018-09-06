from nlu_converters.luis_converter import LuisConverter

#convert training data
##luis (also works for rasa)
luis_converter = LuisConverter()
luis_converter.import_corpus("./corpus/raw/ChatbotCorpus.json")
luis_converter.export("ChatbotCorpus_Luis.json")
