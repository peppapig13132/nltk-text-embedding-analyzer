import nltk
from sentence_transformers import SentenceTransformer
from nltk import pos_tag, word_tokenize

# # Download NLTK resources
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def is_first_person(sentence):
    """
    Check if the sentence is written in the first person.
    """
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    
    # Tag each word with a part of speech (POS)
    pos_tags = pos_tag(words)
    
    # List of first-person subject pronouns (lowercase)
    first_person_pronouns = ['i', 'we']
    
    # Check if the first word is a verb (imperative sentences usually start with a verb)
    if pos_tags[0][1].startswith('VB'):
        return False  # Consider it an imperative sentence, hence not first person
    
    # Iterate through the POS tags to find first-person pronouns followed by verbs
    for i, (word, tag) in enumerate(pos_tags):
        if word.lower() in first_person_pronouns:
            # Check if the next sibling (next word) is a verb (tag starts with 'VB')
            if i + 1 < len(pos_tags) and pos_tags[i + 1][1].startswith('VB'):
                return True
    
    return False

def is_actionable(sentence):
    """
    Check if the sentence is actionable.
    An actionable sentence typically contains verbs in base form or modal verbs.
    """
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    # Look for verbs
    action_verbs = {tag for word, tag in tagged if tag.startswith('VB')}
    return len(action_verbs) > 0


def analyze_sentence(sentence):
    first_person = is_first_person(sentence)
    actionable = is_actionable(sentence)

    return first_person and actionable


def analyze_sentences(sentences):
    """
    Analyze a list of sentences and return a list indicating whether each is in first person.
    """
    results = []
    for sentence in sentences:
        result = analyze_sentence(sentence)
        results.append(result)
    return results


# Example usage
sentences = [
    "Be punctual for meetings and respect agreed-upon deadlines.",
    "Provide space for reflection if you notice I'm processing a difficult situation.",
    "I prefer group discussions over private conversations for most work matters.",
    "Engage in brief social chat at the start of meetings to build rapport.",
    "I'm willing to change course if presented with compelling arguments."
]
result = analyze_sentences(sentences)
print(result)