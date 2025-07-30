import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Test dataset with known financial entities
test_comments = [
    "Just bought Tesla calls, let's go!",
    "SPY is going to the moon!",
    "Apple earnings gonna be huge",
    "Why is Microsoft dumping so hard?",
    "YOLO'd into Amazon calls",
    "Google is breaking resistance",
    "Netflix puts printing money",
    "Meta to the moon!",
    "Nvidia squeeze incoming",
    "AMD diamond hands until $200",
    "JPMorgan looks bullish",
    "Goldman Sachs is overvalued",
    "Fed gonna tank the market",
    "Powell speaking today",
    "Rate cut priced in for QQQ",
    "Inflation data will affect SPY",
    "Berkshire Hathaway long term play",
    "Johnson & Johnson dividend play",
    "Pfizer calls for earnings",
    "Coca-Cola stable investment",
]

# Expected entities we want to extract (ground truth)
expected_entities = [
    ["Tesla"],
    ["SPY"],
    ["Apple"],
    ["Microsoft"],
    ["Amazon"],
    ["Google"],
    ["Netflix"],
    ["Meta"],
    ["Nvidia"],
    ["AMD"],
    ["JPMorgan"],
    ["Goldman Sachs"],
    ["Fed"],
    ["Powell"],
    ["QQQ"],
    ["SPY"],
    ["Berkshire Hathaway"],
    ["Johnson & Johnson"],
    ["Pfizer"],
    ["Coca-Cola"],
]

print("🧪 Testing Financial Entity Recognition Accuracy")
print("=" * 50)

correct_extractions = 0
total_expected = 0

for i, comment in enumerate(test_comments):
    doc = nlp(comment)

    # Extract entities
    extracted = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PERSON", "GPE"]]
    expected = expected_entities[i]

    # Check if we found the expected entities
    found_expected = any(
        exp.lower() in [ext.lower() for ext in extracted] for exp in expected
    )

    if found_expected:
        correct_extractions += 1

    total_expected += 1

    print(f"Comment: {comment}")
    print(f"Expected: {expected}")
    print(f"Extracted: {extracted}")
    print(f"Match: {'✅' if found_expected else '❌'}")
    print("-" * 30)

accuracy = (correct_extractions / total_expected) * 100
print(f"\n📊 RESULTS:")
print(f"Correct Extractions: {correct_extractions}/{total_expected}")
print(f"Accuracy: {accuracy:.1f}%")

print(f"\n💼 RESUME METRIC:")
print(
    f'"Named Entity Recognition achieving {accuracy:.0f}% accuracy in financial entity extraction"'
)
