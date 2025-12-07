def problem1():
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    iso_dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', dates_text)

    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    pattern_email = r'(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+\.\w+)'
    email_parts = [{'username': m.group('username'), 'domain': m.group('domain')} for m in re.finditer(pattern_email, emails_text)]

    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    pattern_phone = r'\(?(\d{3})\)?[-.\s]?(\d{3}-\d{4})'
    phone_numbers = re.findall(pattern_phone, phones_text)

    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    pattern_repeated = r'\b(\w+)\s+\1\b'
    repeated_words = [m.group(1) for m in re.finditer(pattern_repeated, repeated_text, re.IGNORECASE)]

    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }
