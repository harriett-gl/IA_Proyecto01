import re

STOP_WORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
    "your", "yours", "yourself", "yourselves", "he", "him", "his",
    "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which",
    "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having",
    "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while", "of", "at", "by", "for",
    "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "any",
    "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "can", "will", "just", "should", "now",
    "el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una",
    "por", "para", "con", "que", "mi", "se", "es"
}


def simple_stem(word):
    suffixes = ["ing", "ed", "ly", "es", "s", "ment"]
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    return word


def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z\s]", " ", texto)
    palabras = texto.split()
    palabras = [p for p in palabras if p not in STOP_WORDS]
    palabras = [simple_stem(p) for p in palabras]
    return palabras
