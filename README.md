🎬 IMDB Movie Review Sentiment Analyzer

A Deep Learning based Sentiment Analysis Web App built using TensorFlow, Simple RNN, and Streamlit.
The application predicts whether a movie review is Positive 😊 or Negative 😞.

This project uses the IMDB Movie Review Dataset and a pre-trained Simple RNN model to classify user input reviews.

🚀 Features

🎬 Analyze movie review sentiment

🧠 Deep Learning model using Simple RNN

⚡ Real-time prediction with Streamlit UI

📝 Example reviews for quick testing

📊 Confidence score display

📱 Simple and clean interface

🧠 Model Information

Model Type: Simple Recurrent Neural Network (RNN)
Dataset: IMDB Movie Reviews Dataset
Framework: TensorFlow / Keras

The model processes text reviews by:

  1.Converting words to numerical tokens

  2.Padding sequences to fixed length

  3.Feeding them into a trained RNN model

  4.Predicting sentiment score

Score interpretation:

  * > 0.5 → Positive Review

  * ≤ 0.5 → Negative Review

🖥️ Application Interface

## Application Screenshots
<table>
<tr>
<td align="center">
<img src="https://github.com/bhautik2005/imdb-sentiment-analyzer-/blob/96f9fcac160a5f5272c0b626d26e9c5cd3c439c1/Screenshot%202026-02-28%20120530.png" width="450"><br>
 
</td>

<td align="center">
<img src="https://github.com/bhautik2005/imdb-sentiment-analyzer-/blob/96f9fcac160a5f5272c0b626d26e9c5cd3c439c1/Screenshot%202026-02-28%20120730.png" width="450"><br>
 
</td>
</tr>

<tr>
<td align="center">
<img src="https://github.com/bhautik2005/imdb-sentiment-analyzer-/blob/96f9fcac160a5f5272c0b626d26e9c5cd3c439c1/Screenshot%202026-02-28%20120814.png" width="450"><br>
 
</td>

<td align="center">
<img src="
https://github.com/bhautik2005/imdb-sentiment-analyzer-/blob/96f9fcac160a5f5272c0b626d26e9c5cd3c439c1/Screenshot%202026-02-28%20120903.png" width="450"><br>
 
</td>
</tr>
</table>

<img src="https://github.com/bhautik2005/imdb-sentiment-analyzer-/blob/96f9fcac160a5f5272c0b626d26e9c5cd3c439c1/output.png" width="750">

The Streamlit application allows users to:

  --> Enter their own movie review

  --> Select example reviews

  --> Click Classify to get sentiment prediction

View prediction confidence

📂 Project Structure
IMDB-Sentiment-Analyzer
│
├── app.py                 # Streamlit Application
├── simple_rnn_imdb2.h5    # Trained RNN model
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
⚙️ Installation

Clone the repository:

git clone https://github.com/bhautik2005/Movies_rives_prdiction
cd imdb-sentiment-analyzer

Install dependencies:

pip install -r requirements.txt
▶️ Run the Application
streamlit run main.py

After running, open the browser:

http://localhost:8501
📦 Requirements

requirements.txt

tensorflow==2.15.0
pandas
numpy
scikit-learn
tensorboard
matplotlib
streamlit
scikeras
📊 Example Reviews

Positive Example

This movie was absolutely fantastic, the acting was brilliant and the story was very engaging.

Negative Example

Worst movie ever. Completely boring and waste of time.
🔮 Future Improvements

Possible improvements:

 1.Add Transformer / BERT based model

 2.Deploy on Streamlit Cloud

 3.Add confidence visualization

4 .Add review history

 5.Improve UI design

🛠️ Technologies Used

Python

TensorFlow / Keras

Streamlit

NumPy

Scikit-Learn

Matplotlib

👨‍💻 Author

Bhautik Gondaliya

AI / ML & Backend Developer
Interested in Generative AI, Machine Learning, and Full Stack Development
