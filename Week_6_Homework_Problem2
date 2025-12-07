def problem2():
    files_text = """ Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css """
    pattern_images = r'\b\w+\.(?:jpg|jpeg|png|gif)\b'
    image_files = re.findall(pattern_images, files_text, re.IGNORECASE)

    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    pattern_dates = r'\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|[A-Z][a-z]+ \d{1,2}, \d{4})\b'
    all_dates = re.findall(pattern_dates, mixed_dates)

    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    pattern_prices = r'\$[\d\.]+|USD \d+\.?\d*|\d+ dollars|€[\d\.]+|£[\d\.]+'
    prices = re.findall(pattern_prices, prices_text)

    code_text = """ We use Python for data science, Java for enterprise apps, JavaScript or JS for web development, and C++ or CPP for systems. """
    pattern_langs = r'\bPython|Java|JavaScript|JS|C\+\+|CPP\b'
    languages = re.findall(pattern_langs, code_text)

    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }
