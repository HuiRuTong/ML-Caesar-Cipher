import numpy as np
import tensorflow as tf

alphabet = " \nabcdefghijklmnopqrstuvwxyz"  # Indices represent the numerical counterpart to a char

training_files = ["1984", "A_Brief_History_Of_Time", "Alice_In_Wonderland","Bee_Movie_Script",
                "Beyond_Good_And_Evil", "I_Have_A_Dream", "Language", "Particle_Physics_Britanica",
                "Prions_Wikipedia", "Shrek_Script", "The_Metamorphosis", "To_Kill_A_Mockingbird"]
sentences = []
labels = []

"""
Converts the characters in a sentence into their numerical counterparts, preserving spaces and newlines
"""
def Pre_process(encrypted_txt):
    tokenise = tf.keras.preprocessing.text.Tokenizer(char_level=True)

    tokenise.fit_on_texts(alphabet)
    converted_txt = tokenise.texts_to_sequences(encrypted_txt)
    
    processed_txt = tf.keras.utils.pad_sequences(converted_txt, maxlen=500, padding="post") # Padding is required for conversion to ndarray
    return processed_txt

for f in training_files:
    label_path = "Training_labels\\" + f + "_label.txt"
    encrypted_path = "Training_data\\" + f + "_encrypted.txt"

    label = open(label_path, 'r', encoding="utf-8")
    encrypted = open(encrypted_path, 'r', encoding="utf-8")
    for l in label:
        labels.append(int(l.replace('\n', '')) - 1)
    for l in encrypted:
        sentences.append(l)

    label.close()
    encrypted.close()

dataset = np.array(tf.keras.utils.pad_sequences([Pre_process(s for s in sentences)], padding="post"), dtype=np.int32)   # Some files have less sentences than others so we need to pad them out with empty sentences
keys = np.array(labels, dtype=np.int32)
dataset = np.reshape(dataset, (dataset.size // 500, 500))   # Dataset is a 3D array but the 3rd dimension isn't useful so convert it to 2D

sentences.clear()   # Used later for the testing data
labels.clear()

"""
Stuff for testing the model
"""
testing_files = ["Neural_Networks_IBM", "Pigeons", "Tuberculosis", "The_Iliad"]
for f in testing_files:
    label_path = "Testing_labels\\" + f + "_label.txt"
    encrypted_path = "Testing_data\\" + f + "_encrypted.txt"

    label = open(label_path, 'r', encoding='utf-8')
    encrypted = open(encrypted_path, 'r', encoding='utf-8')
    for l in label:
        labels.append(int(l.replace('\n', '')) - 1)
    for l in encrypted:
        sentences.append(l)

    label.close()
    encrypted.close()

test_data = np.array(tf.keras.utils.pad_sequences([Pre_process(s for s in sentences)], padding="post"), dtype=np.int32)
test_keys = np.array(labels, dtype=np.int32)
test_data = np.reshape(test_data, (test_data.size // 500, 500))

"""
Model structure
"""
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Embedding(29, 25))
model.add(tf.keras.layers.Masking(0))   # Tells the model to ignore the padded 0s
model.add(tf.keras.layers.LSTM(256))
model.add(tf.keras.layers.Dropout(0.4)) # High dropout rate to prevent / minimise overfitting
model.add(tf.keras.layers.Dense(25, activation="softmax"))
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(dataset, keys, epochs=100, batch_size=16, validation_split=0.4)
model.save("cipher_model2.keras")

model.evaluate(test_data, test_keys)