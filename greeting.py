import pickle

with open('male_endings.pkl', 'rb') as f:
    male_endings = pickle.load(f)
with open('female_endings.pkl', 'rb') as f:
    female_endings = pickle.load(f)

    
def greeting(name: str) -> str:
    if name[-4:].lower() in male_endings:
        return f'Уважаемый {name}'
    if name[-4:].lower() in female_endings:
        return f'Уважаемая {name}'
    raise ValueError('Can\'t resolve gender')
