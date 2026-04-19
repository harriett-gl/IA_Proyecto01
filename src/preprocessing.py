import re
import unicodedata

SPANISH_TO_ENGLISH = {
    "pedido": "order",
    "orden": "order",
    "ordenes": "order",
    "compra": "order",
    "compras": "order",
    "cancelar": "cancel",
    "cancelacion": "cancel",
    "cancelación": "cancel",
    "cuenta": "account",
    "factura": "invoice",
    "facturacion": "invoice",
    "facturación": "invoice",
    "cobro": "payment",
    "cobros": "payment",
    "pago": "payment",
    "pagos": "payment",
    "reembolso": "refund",
    "devolucion": "refund",
    "devolución": "refund",
    "envio": "shipping",
    "envíos": "shipping",
    "envios": "shipping",
    "entrega": "delivery",
    "contacto": "contact",
    "suscripcion": "subscription",
    "suscripción": "subscription",
    "retroalimentacion": "feedback",
    "comentario": "feedback",
    "opinion": "feedback",
    "dirección": "address",
    "direccion": "address",
    "correo": "email",
    "paquete": "package",
    "producto": "product",
}

STOP_WORDS = {
    # English
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself",
    "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
    "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if", "or", "because", "as",
    "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after",
    "above", "below", "to", "from", "up", "down", "in", "out", "on",
    "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than", "too", "very", "can", "will",
    "just", "should", "now", "please", "hi", "hello",
    # Spanish
    "yo", "tu", "tú", "usted", "ustedes", "nosotros", "nosotras",
    "ellos", "ellas", "mi", "mis", "tu", "tus", "su", "sus",
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "desde", "hasta", "hacia", "por", "para", "con", "sin",
    "sobre", "entre", "contra", "en", "a", "y", "e", "o", "u", "ni",
    "que", "como", "si", "porque", "pues", "aunque", "mientras", "cuando",
    "donde", "es", "son", "soy", "eres", "somos", "fui", "fue", "fueron",
    "era", "eran", "ser", "estar", "estoy", "esta", "está", "estan",
    "están", "estaba", "estaban", "tener", "tengo", "tiene", "tienen",
    "hacer", "hago", "hace", "hacen", "se", "le", "les", "te", "me",
    "nos", "ya", "aun", "aún", "solo", "sólo", "muy", "mas", "más",
    "menos", "tambien", "también", "hola", "buenas", "buenos", "dias",
    "días", "tardes", "noches", "gracias", "favor"
}


def quitar_acentos(texto):
    return "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )


def simple_stem(palabra):
    sufijos = ["ingly", "edly", "ing", "edly", "ed", "ies", "es", "s", "ment"]
    for sufijo in sufijos:
        if palabra.endswith(sufijo) and len(palabra) > len(sufijo) + 2:
            if sufijo == "ies":
                return palabra[:-3] + "y"
            return palabra[:-len(sufijo)]
    return palabra


def normalizar_token(token):
    token = SPANISH_TO_ENGLISH.get(token, token)
    token = simple_stem(token)
    return token


def limpiar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"\{\{.*?\}\}", " ", texto)
    texto = quitar_acentos(texto)
    texto = re.sub(r"[^a-z0-9\s']", " ", texto)
    palabras = []

    for token in texto.split():
        if len(token) <= 1:
            continue
        if token in STOP_WORDS:
            continue
        token = normalizar_token(token)
        if len(token) <= 1 or token in STOP_WORDS:
            continue
        palabras.append(token)

    # Bigramas simples para capturar contexto
    bigramas = [
        f"{palabras[i]}_{palabras[i + 1]}"
        for i in range(len(palabras) - 1)
    ]

    return palabras + bigramas
