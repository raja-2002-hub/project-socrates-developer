import pandas as pd

def load_dataset():
    data = {
        "question": [
            "Is it ever okay to lie?", "What makes an action morally right?",
            "What is a valid argument?", "Can logic prove everything?",
            "Do we have free will?", "What is the nature of time?",
            "What is knowledge?", "Can we ever be certain of anything?",
            "What is justice in society?", "Is democracy the best form of government?",
            "Can AI be truly intelligent?", "Will AI replace human jobs?"
        ],
        "category": [
            "Ethics", "Ethics", "Logic", "Logic",
            "Metaphysics", "Metaphysics", "Epistemology", "Epistemology",
            "Politics", "Politics", "AI", "AI"
        ]
    }
    return pd.DataFrame(data)
