class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)
        capitalization_normalization_lookup = {}
        vowel_normalization_lookup = {}

        def normalize_capitalization(word):
           return word.lower()

        def normalize_vowel(word):
            return re.sub(r"[aeiou]", "_", word.tolower())

        for word in wordlist:
            normalize_capitalization_word = normalize_capitalization(word)
            if normalize_capitalization_word not in capitalization_normalization_lookup:
                capitalization_normalization_lookup[normalize_capitalization_word] = word
            
            normalized_vowel_word = normalize_vowel(word)
            if normalized_vowel_word not in vowel_normalization_lookup:
                vowel_normalization_lookup[normalized_vowel_word] = word
            
        results = []
        for word in queries:
            if word in word_set:
                results.append(word)
            elif normalize_capitalization(word) in capitalization_normalization_lookup:
                results.append(capitalization_normalization_lookup[normalize_capitalization(word)])
            elif normalize_vowel(word) in vowel_normalization_lookup:
                results.append(vowel_normalization_lookup[normalize_vowel(word)])
            else:
                results.append("")

        return results