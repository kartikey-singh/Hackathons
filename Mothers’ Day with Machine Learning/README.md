# HackerEarth Machine Learning challenge: Mothers’ Day with Machine Learning

## Implementation Details:

- Used TensorFlow2
- NLP Domain Task Visualisations
- Word Counts for each class, and unique types counts
- Tree of most common words
- Word Cloud for each class

### Modelling 1:
- Using word embeddings nnlm english 128 dimensions
- Plotted various losses and accuarcy functions

### Modelling 2: Embedding layer model
- Similar to previous one

### Modelling 3: Embedding + LSTM model
- Used LSTM/GRU with previous versions
- As dataset is imbalanced, used different class weightage

### Modelling 4: Ensembling LSTM Networks
- For each class creates its one vs all dataset and train on them
- Ensemble the predictions that you get.

Secured Rank: 147 out of 3276 participants.

