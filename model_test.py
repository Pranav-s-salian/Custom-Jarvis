import json
import pickle

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
model = tf.keras.models.load_model("chat_model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

with open("intents.json") as file:
    data = json.load(file)

def preprocess_input(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, truncating='post', maxlen=20)
    return padded_sequences

def get_response(user_input):
    processed_input = preprocess_input(user_input)
    prediction = model.predict(processed_input)
    predicted_label = np.argmax(prediction)
    response_tag = label_encoder.inverse_transform([predicted_label])[0]
    
    confidence = prediction[0][predicted_label]
    if confidence < 0.7:
        return {
            "response": "Sorry, I didn't understand that.",
            "confidence": confidence,
            "predicted_tag": response_tag,
            "predictions": prediction.tolist()
        }

    for intent in data['intents']:
        if intent['tag'] == response_tag:
            return {
                "response": np.random.choice(intent['responses']),
                "confidence": confidence,
                "predicted_tag": response_tag,
                "predictions": prediction.tolist()
            }

    return {
        "response": "Sorry, I didn't understand that.",
        "confidence": confidence,
        "predicted_tag": response_tag,
        "predictions": prediction.tolist()
    }


while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    result = get_response(user_input)
    print(f" the response is {result["response"]}")
    