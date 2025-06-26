from pdfminer.high_level import extract_text
import sys

KEYWORDS = [
    'Python', 'SQL', 'Machine Learning', 'Deep Learning', 'NLP', 'Data Analysis',
    'Data Visualization', 'TensorFlow', 'Keras', 'Pandas', 'NumPy', 'Scikit-learn',
    'Power BI', 'Tableau', 'Git', 'AWS', 'Azure', 'REST API', 'Flask', 'Docker'
]

def extract_text_from_pdf(file_path):
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print("Error reading PDF:", e)
        sys.exit(1)

def analyze_keywords(text):
    counts = {}
    for keyword in KEYWORDS:
        counts[keyword] = text.lower().count(keyword.lower())
    return counts

def suggest_improvements(counts):
    suggestions = [kw for kw, count in counts.items() if count == 0]
    return suggestions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resume_analyzer.py <path_to_resume.pdf>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = extract_text_from_pdf(file_path)
    keyword_counts = analyze_keywords(text)

    print("\n📊 Keyword Counts:")
    for keyword, count in keyword_counts.items():
        print(f"{keyword}: {count}")

    missing = suggest_improvements(keyword_counts)
    if missing:
        print("\n💡 Suggested Improvements:")
        for kw in missing:
            print(f"- Add more about: {kw}")
    else:
        print("\n✅ Your resume covers all key skills!")

