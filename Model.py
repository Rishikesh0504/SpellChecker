import language_tool_python
from textblob import TextBlob

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.tool = language_tool_python.LanguageTool('en-US')  # US English language model

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.tool.check(text)
        foundmistakes = []
        for match in matches:
            foundmistakes.append(match.ruleIssueType)  # or `match.replacement` for suggested fixes
        foundmistakes_count = len(foundmistakes)
        return foundmistakes, foundmistakes_count
