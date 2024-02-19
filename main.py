# main.py
from utility import tokenize, tokenize_with_split, highlight_differences

def main():
    # Inputs
    original_text = """Hello World. 
This is the first text."""

    edited_text = """Hi World!
This is the second text!"""

    ### 1. Character-Level Text Difference
    original_highlighted, edited_highlighted = highlight_differences(original_text, edited_text)

    # Print the results
    print("1. Character-Level Text Difference")
    print("Original Text:")
    print(original_highlighted)
    print("\nEdited Text:")
    print(edited_highlighted)
    print("-"*80)

    ### 2. Word-Level Text Difference
    # Tokenize the input texts with split()
    tokens1 = tokenize_with_split(original_text)
    tokens2 = tokenize_with_split(edited_text)

    original_highlighted, edited_highlighted = highlight_differences(tokens1, tokens2)
    # Print the results
    print("2. Word-Level Text Difference")
    print("Original Text:")
    print(original_highlighted)
    print("\nEdited Text:")
    print(edited_highlighted)
    print("-"*80)

    ### 3. Token-Level Text Difference
    # Tokenize the input texts
    tokens1 = tokenize(original_text)
    tokens2 = tokenize(edited_text)

    # Highlight differences between the two sets of tokens
    original_highlighted, edited_highlighted = highlight_differences(tokens1, tokens2)

    # Print the results
    print("3. Token-Level Text Difference")
    print("Original Text:")
    print(original_highlighted)
    print("\nEdited Text:")
    print(edited_highlighted)

if __name__ == "__main__":
    main()