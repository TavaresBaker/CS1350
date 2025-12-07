def problem4():
    messy_phones = """ Contact list: - John: 555.123.4567 - Jane: (555) 234-5678 - Bob: 555 345 6789 - Alice: 5554567890 """
    def standardize_phones(text):
        pattern = r'\b(?:\(?(\d{3})\)?[-.\s]?)(\d{3})[-.\s]?(\d{4})\b'
        replacement = r'(\1) \2-\3'
        return re.sub(pattern, replacement, text)
    cleaned_phones = standardize_phones(messy_phones)

    sensitive_text = """ Customer: John Doe SSN: 123-45-6789 Credit Card: 4532-1234-5678-9012 Email: john.doe@email.com Phone: (555) 123-4567 """
    def redact_sensitive(text):
        text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', text)
        text = re.sub(r'\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b', 'XXXX-XXXX-XXXX-XXXX', text)
        return text
    redacted_text = redact_sensitive(sensitive_text)

    markdown_text = """ Check out [Google](https://google.com) for search. Visit [GitHub](https://github.com) for code. Read documentation at [Python Docs](https://docs.python.org). """
    def markdown_to_html(text):
        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    html_text = markdown_to_html(markdown_text)

    template = """ Dear {name}, Your order #{order_id} for {product} has been shipped. Tracking number: {tracking} """
    values = { 'name': 'John Smith', 'order_id': '12345', 'product': 'Python Book', 'tracking': 'TRK789XYZ' }
    def fill_template(template, values):
        return re.sub(r'\{(\w+)\}', lambda m: values[m.group(1)], template)
    filled_template = fill_template(template, values)

    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }
