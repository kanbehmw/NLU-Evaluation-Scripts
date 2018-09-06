from nlu_analysers.rasa_analyser import RasaAnalyser

##rasa
rasa_analyser = RasaAnalyser("http://localhost:5000/parse", "chatbot")
rasa_analyser.get_annotations("./corpus/raw/ChatbotCorpus.json", "ChatbotAnnotations_Rasa.json")
rasa_analyser.analyse_annotations("ChatbotAnnotations_Rasa.json", "./corpus/raw/ChatbotCorpus.json", "ChatbotAnalysis_Rasa.json")

