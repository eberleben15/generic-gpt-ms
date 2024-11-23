# config.py
MODEL_NAME = 'distilbert-base-uncased'
DEFAULT_MAX_LENGTH = 50
DEFAULT_STYLE = 'friendly'

STYLE_PRESETS = {
    'friendly': {
        'temperature': 0.7,
        'max_length': 50
    },
    'formal': {
        'temperature': 0.3,
        'max_length': 70
    },
    'technical': {
        'temperature': 0.9,
        'max_length': 100
    }
}
# Add a default context setting
DEFAULT_CONTEXT = "You are a model that responds in a straightforward manner."