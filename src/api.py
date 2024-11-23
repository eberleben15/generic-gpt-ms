# api.py
from flask import Flask, request, jsonify
from transformers import pipeline
from config import MODEL_NAME, DEFAULT_MAX_LENGTH, DEFAULT_STYLE, STYLE_PRESETS, DEFAULT_CONTEXT

def create_app():
    app = Flask(__name__)
    chat_model = pipeline('text-generation', model=MODEL_NAME)

    @app.route('/set_context', methods=['POST'])
    def set_context():
        data = request.get_json()
        context_prompt = data.get('context_prompt', DEFAULT_CONTEXT)
        response = chat_model(context_prompt, max_length=100)
        return jsonify({'response': 'Context set successfully', 'details': response[0]['generated_text']}), 200

    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.get_json()
        prompt = data.get('prompt')
        style = data.get('style', DEFAULT_STYLE)
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        style_settings = STYLE_PRESETS.get(style, {})
        temperature = style_settings.get('temperature', 0.7)
        max_length = style_settings.get('max_length', DEFAULT_MAX_LENGTH)

        full_prompt = f"{request.context} {prompt}"  # Prepend the stored context to the prompt
        response = chat_model(full_prompt, max_length=max_length, temperature=temperature)
        return jsonify({'response': response[0]['generated_text']}), 200

    return app