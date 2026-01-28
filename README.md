# A ML Approach to Solving the Caesar Cipher
Why aim for reliable, easy-to-implement solutions when you can solve all your problems with machine learning?
This was written as my final project for a machine learning class I took.

I'm no good at formal explanations, so the gist of it is this:
The program uses a basic machine learning algorithm (LSTM) to learn to
"read" text that has been encrypted with a Caesar cipher, allowing
it to decipher such ciphers with high accuracy. I acknowledge that
this is the equivalent of calculating 1+1 with a quantum computer (uncertainties
and all!), but making another stock market predictor seemed
really boring.


## How it works:
1. **Acquiring training data**

Online texts from a wide variety of genres were chosen in order to ensure that
the model wouldn't be biased towards one form of writing. To maximise training
data, each body of text was split into sentences using NLTK's tokeniser and
then encrypted with a different cipher.

2. **Encrypting**

The shift (1-25) amount for the cipher of each sentence is randomly generated
using randint(), which gives a uniform distribution of shifts, again ensuring that
the model won't be biased. Once the shift is chosen, it is noted down in a separate
label file to be used for training later on. Then, encrypt.py goes through
each letter of each sentence and shifts it forward. Spaces, newlines and punctuation
are kept intact to preserve a semblance of context and grammar.

3. **Training**

To prepare the text for actual training, it needs to be numerical so TF's tokeniser
is used to convert characters and punctuations into integers. LSTM, in particular,
was chosen for the model's structure so it can remember certain patterns that
occur much earlier in its training data. This allows it to better recognise the
aforementioned context and grammar rules, making it the default for language
processing tasks. [Though if you're reading this, you likely already knew that]

4. **Testing**

The model is tested and shows an accuracy of 97-98%. Although, it's likely that
more data is needed to really evaluate its performance.

5. **Decrypting**

A copy of the model is saved and can be used anytime to decrypt Caesar ciphers.
Like any product of machine learning, of course, it's not perfect. The model does
well enough for most modern English, but it struggles with older forms of writing
(evaluated on The Iliad), likely due to a gap in its training set. Moreover, it's
awful at decrypting short, one-or-two-word sentences, though this isn't too big
of an issue. Realistically, who's encrypting "Hello there."?



## User Instructions:
-  encrypt.py encrypts any piece of .txt you give it. To encrypt a .txt file,
    place it inside the "Texts" folder and run the program in powershell using
    ```bash
    encrypt.py <name of file without .txt>
    ```
    without the <>.

-  main.py is where the model is trained and evaluated. If you only intend to
    use it for decryption purposes, you won't ever need to interact with This
    file. However, should you want to retrain the model yourself, just run
    this program using
    ```bash
    main.py
    ```

-  decrypt.py loads a trained model and uses it to decrypt a given .txt file.
    To decrypt a .txt file, run the program in powershell using
    ```bash
    decrypt.py <filepath>
    ```
    without the <>. Note that unlike encrypt.py, you need to provide the **full
    file path** rather than just the name.
