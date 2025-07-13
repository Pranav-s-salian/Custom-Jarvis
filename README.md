JARVIS - Advanced AI Assistant 🤖<img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg">
<img alt="Made with Python" src="https://img.shields.io/badge/Made with-Python-1f425f.svg">
<img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-2.x-orange">
<img alt="Ollama" src="https://img.shields.io/badge/Ollama-Integrated-blue">
<div align="center"> <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmZiMzM4ZTM4ZjBjOWNmZDM3N2E1ZGY5YjQ3NjJhZjQ5NGJjZTY5YiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/hJ2BmdoT0QP5tJkZlP/giphy.gif" width="300px"/> </div>
🌟 Dual AI Model Architecture
JARVIS implements a hybrid approach using two powerful AI models:

1. Custom LSTM-RNN Model
Built using TensorFlow/Keras
Trained on custom dataset (intents.json)
Specialized for quick, task-specific responses
Offline capability

Files: chat_model.h5, tokenizer.pkl, label_encoder.pkl

3. Ollama Integration
Uses Llama 3.2 model
Handles complex, contextual conversations
More flexible and adaptable responses
Requires internet connection
Implementation in JARVIS.PY

🛠️ Technical Stack
<div align="center"> <table> <tr> <td align="center"><img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" width="40"/><br>TensorFlow</td> <td align="center"><img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" width="40"/><br>Python</td> <td align="center"><img src="https://www.vectorlogo.zone/logos/keras/keras-icon.svg" width="40"/><br>Keras</td> <td align="center"><img src="https://avatars.githubusercontent.com/u/95862902" width="40"/><br>Ollama</td> </tr> </table> </div>

📋 Features
🗣️ Voice Recognition & Synthesis
🤖 Dual AI Model Processing
⚡ Fast Response Time
📅 Date & Time Management
😄 Joke Telling Capability
🎯 Context-Aware Responses
💡 System Control Functions
🔄 Fallback Mechanism between Models

🚀 Quick Start
# Clone the repository
git clone https://github.com/Pranav-s-salian/Custom-Jarvis.git
cd Custom-Jarvis

# Install requirements
pip install -r requirements.txt

# Install Ollama (if not already installed)
# Visit: https://ollama.ai/download

# Pull Llama model
ollama pull llama2

# Train custom model (optional if using pre-trained)
python model_train.py

# Start JARVIS
python JARVIS.PY

🚀 Quick Start
📊 Model Selection Logic

def smart_response(user_input):
    Try custom model first
    confidence = get_custom_model_confidence(user_input)
    
    if confidence > 0.7:
        return custom_model_response(user_input)
    else:
        return ollama_response(user_input)
        
🎯 Intent Categories
Currently supports various intents including:

👋 Greetings
👋 Goodbyes
⏰ DateTime queries
😄 Jokes
🙏 Thanks
❓ Identity questions
💬 General conversation
📝 Custom Model Training Data
Example from intents.json:

🔧 Configuration
Key files:

JARVIS.PY: Main assistant code
model_train.py: Custom model training

intents.json: Training data

chat_model.h5: Trained model

tokenizer.pkl: Text preprocessing

label_encoder.pkl: Intent classification

🆕 Adding New Features
Add new intents to intents.json
Retrain the model

Implement new functions in JARVIS.PY
Test with both models

📈 Performance Comparison

Feature	Custom Model	Ollama
Response Time	<100ms	~1s
Memory Usage	~100MB	~2GB
Accuracy	95%*	90%*
Offline Use	✅	❌
*For supported intents

🤝 Contributing
Fork the repo
Create feature branch
Commit changes
Push to branch
Create Pull Request
🔮 Future Enhancements
<input disabled="" type="checkbox"> Multi-language support
<input disabled="" type="checkbox"> GUI interface
<input disabled="" type="checkbox"> Emotion detection
<input disabled="" type="checkbox"> API integration
<input disabled="" type="checkbox"> Custom wake word
<input disabled="" type="checkbox"> Smart home control
📄 License
MIT License - feel free to use and modify!

👨‍💻 Author
Created by Pranav s salian

<div align="center"> ⭐ Star this repo if you find it helpful! ⭐
For issues and feature requests, create an issue

</div>
