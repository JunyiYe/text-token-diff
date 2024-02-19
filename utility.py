import difflib
import spacy

# Load the English tokenizer from spaCy
nlp = spacy.load("en_core_web_sm")

def tokenize(text):
    """
    Tokenizes the input text using spaCy, including spaces as separate tokens.

    :param text: The input text to tokenize.
    :return: A list of tokens, including spaces.
    """
    doc = nlp(text)
    tokens = []

    for token in doc:
        tokens.append(token.text)
        if token.whitespace_:
            tokens.append(' ')
    
    return tokens

def tokenize_with_split(text):
    """
    Tokenizes the input text at word-level using the split method, including spaces as separate tokens.
    
    This function splits the text into words based on spaces and then adds a space token (' ')
    after each word except the last one to mimic the behavior of keeping spaces as tokens.
    
    :param text: The input text to tokenize.
    :return: A list of tokens, where each word and space is a separate token.
    """
    words = text.split()  # Split the text into words based on spaces
    tokens = []
    
    for word in words[:-1]:  # Iterate through words, excluding the last one
        tokens.append(word)  # Add the word to the tokens list
        tokens.append(' ')   # Add a space as a separate token
    
    if words:  # Check if the list is not empty to avoid IndexError
        tokens.append(words[-1])  # Add the last word without a following space
    
    return tokens

def highlight_differences(original, edited):
    """
    Highlights the differences between two lists of tokens.

    :param original: The original list of tokens.
    :param edited: The edited list of tokens.
    :return: A tuple containing two strings: the highlighted original and edited texts.
    """
    diff = list(difflib.ndiff(original, edited))
    original_highlighted = ""
    edited_highlighted = ""
    
    for word in diff:
        if word.startswith("- "):
            original_highlighted += f"\033[91m{word[2:]}\033[0m"
        elif word.startswith("+ "):
            edited_highlighted += f"\033[92m{word[2:]}\033[0m"
        elif word.startswith("  "):
            original_highlighted += f"{word[2:]}"
            edited_highlighted += f"{word[2:]}"

    return original_highlighted.strip(), edited_highlighted.strip()

