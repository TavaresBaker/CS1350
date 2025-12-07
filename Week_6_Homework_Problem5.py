def problem5():
    class PatternLibrary:
        EMAIL = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$', re.IGNORECASE)
        URL = re.compile(r'^(?:https?://)?[\w.-]+\.\w+(?:/[\w./-]*)?$', re.IGNORECASE)
        ZIP_CODE = re.compile(r'^\d{5}(?:-\d{4})?$')
        PASSWORD = re.compile(r'''
            ^               # start
            (?=.*[a-z])     # lowercase
            (?=.*[A-Z])     # uppercase
            (?=.*\d)        # digit
            (?=.*[!@#$%^&*()_+{}:"<>?]) # special
            .{8,}           # min 8 chars
            $               # end
        ''', re.VERBOSE)
        CREDIT_CARD = re.compile(r'^(?:\d{4}[-\s]?){3}\d{4}$')

    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
    }
    validation_results = {
        'emails': [bool(PatternLibrary.EMAIL.match(e)) for e in test_data['emails']],
        'urls': [bool(PatternLibrary.URL.match(u)) for u in test_data['urls']],
        'zips': [bool(PatternLibrary.ZIP_CODE.match(z)) for z in test_data['zips']],
        'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
        'cards': [bool(PatternLibrary.CREDIT_CARD.match(c)) for c in test_data['cards']],
    }
    return validation_results
