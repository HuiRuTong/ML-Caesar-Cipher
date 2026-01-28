from sys import argv
import numpy as np
import tensorflow as tf

alphabet = " \nabcdefghijklmnopqrstuvwxyz"
def Pre_process(encrypted_txt):
    tokenise = tf.keras.preprocessing.text.Tokenizer(char_level=True)

    tokenise.fit_on_texts(alphabet)
    converted_txt = tokenise.texts_to_sequences(encrypted_txt)
    
    processed_txt = tf.keras.utils.pad_sequences(converted_txt, maxlen=500, padding="post")
    return processed_txt

model = tf.keras.models.load_model("cipher_model.keras")   # Loads the compiled model so we don't have to retrain it every time

text = open(argv[1], 'r')
text_decrypted = open("decrypted.txt", "w+", encoding="utf-8")
results = model.predict(np.array(Pre_process(text)))
text = open(argv[1], 'r')   # Pre_process() closes the file
text.seek(0)

for r in results:
    key = np.argmax(r) + 1  # Predictions are a probability distribution so argmax is used to get the most probable index then add 1 to get the shift amount
    decrypted = ''
    for c in  text.readline():
        if c == ' ' or c == '\n':
            decrypted += c
        else:
            decrypted += chr((ord(c)-97-key) % 26 + 97) # Checking with an example is easier than explaining the formula so go on,, try it!
    text_decrypted.write(decrypted)

text.close()
text_decrypted.close()