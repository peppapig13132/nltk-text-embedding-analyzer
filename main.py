import nltk
from sentence_transformers import SentenceTransformer
from nltk import pos_tag, word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def is_first_person(sentence):
    """
    Check if the sentence is written in the first person.
    """
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    # Define pronouns
    first_person_pronouns = {'I', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours'}
    second_person_pronouns = {'you', 'your', 'yours'}
    third_person_pronouns = {'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'they', 'them', 'their', 'theirs'}

    # Flags to track pronouns
    found_first_person = False
    found_second_person = False
    found_third_person = False

    for word, tag in tagged:
        if word in first_person_pronouns:
            found_first_person = True
        elif word in second_person_pronouns:
            found_second_person = True
        elif word in third_person_pronouns:
            found_third_person = True
            
    return found_first_person and not (found_second_person or found_third_person)


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


# Example usage
sentence = "I'm willing to change course if presented with compelling arguments."
result = analyze_sentence(sentence)
print(result)
