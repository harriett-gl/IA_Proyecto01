import re

STOP_WORDS = {
    # Inglés
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself",
    "she", "her", "hers", "herself",
    "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves",

    "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having",
    "do", "does", "did", "doing",

    "a", "an", "the",
    "and", "but", "if", "or", "because", "as",
    "until", "while",
    "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through",
    "during", "before", "after", "above", "below",
    "to", "from", "up", "down", "in", "out",
    "on", "off", "over", "under",

    "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such",
    "no", "nor", "not", "only", "own",
    "same", "so", "than", "too", "very",
    "can", "will", "just", "should", "now",

    # Español
    "yo", "tu", "tú", "usted", "ustedes",
    "nosotros", "nosotras", "ellos", "ellas",
    "mi", "mis", "mio", "mia", "míos", "mías",
    "tu", "tus", "tuyo", "tuya",
    "su", "sus", "nuestro", "nuestra",

    "el", "la", "los", "las",
    "un", "una", "unos", "unas",
    "lo", "al", "del",

    "de", "desde", "hasta", "hacia",
    "por", "para", "con", "sin",
    "sobre", "entre", "contra",
    "en", "a",

    "y", "e", "o", "u", "ni",
    "que", "como", "si", "porque", "pues",
    "aunque", "mientras", "cuando", "donde",

    "es", "son", "soy", "eres", "somos",
    "fui", "fue", "fueron", "era", "eran",
    "ser", "estar", "estoy", "esta", "está",
    "estan", "están", "estaba", "estaban",

    "tener", "tengo", "tiene", "tienen",
    "hacer", "hago", "hace", "hacen",

    "se", "le", "les", "te", "me", "nos",
    "ya", "aun", "aún", "solo", "sólo",
    "muy", "mas", "más", "menos",
    "tambien", "también",

    # Muy comunes en tickets (ruido)
    "hola", "buenas", "buenos", "dias", "días",
    "tardes", "noches",
    "gracias", "favor",
    "ayuda", "ayudar", "necesito",
    "quiero", "quisiera",
    "problema", "error",
    "consulta", "duda"
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
