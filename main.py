import ktrain
from ktrain import text
print(ktrain.__version__)

DATA_PATH = 'train_data.csv'
# VALID_DATA = 'validation_data.csv'
NUM_WORDS = 50000
MAXLEN = 500

(x_train, y_train), (x_test, y_test), preproc = text.texts_from_csv(DATA_PATH,
                      'message',
                      label_columns = ["class"],
                      val_filepath=None, # if None, 10% of data will be used for validation
                      max_features=NUM_WORDS, maxlen=MAXLEN,
                      ngram_range=1)

model = text.text_classifier('fasttext', (x_train, y_train),
                             preproc=preproc)

learner = ktrain.get_learner(model, train_data=(x_train, y_train), val_data=(x_test, y_test))
learner.autofit(1e-2)
predictor = ktrain.get_predictor(learner.model, preproc)
predictor.save('predictor_fasttext')