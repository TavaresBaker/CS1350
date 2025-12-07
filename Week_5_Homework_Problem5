import re

def clean_text_pipeline(text, operations):
    steps = []
    cleaned = text

    for op in operations:
        if op == 'trim':
            cleaned = cleaned.strip()

        elif op == 'lowercase':
            cleaned = cleaned.lower()

        elif op == 'remove_punctuation':
            cleaned = re.sub(r'[^\w\s]', '', cleaned)

        elif op == 'remove_digits':
            cleaned = re.sub(r'\d+', '', cleaned)

        elif op == 'remove_extra_spaces':
            cleaned = re.sub(r'\s+', ' ', cleaned).strip()

        elif op == 'remove_urls':
            cleaned = re.sub(r'https?://\S+', '', cleaned)

        elif op == 'remove_emails':
            cleaned = re.sub(r'\S+@\S+\.\S+', '', cleaned)

        elif op == 'capitalize_sentences':
            cleaned = '. '.join(s.strip().capitalize() for s in re.split(r'\.\s*', cleaned) if s)

        steps.append((op, cleaned))

    return {
        'original': text,
        'cleaned': cleaned,
        'steps': steps
    }
