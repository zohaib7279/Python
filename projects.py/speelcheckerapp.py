from speelcheckerapp import SpellChecker
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    
    def correct_text(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}'")
                corrected_words.append(corrected_word)
        
        return'' .join(corrected_words)
    
    def run(self):
        print("/n----SPELL CHECKER APP----")