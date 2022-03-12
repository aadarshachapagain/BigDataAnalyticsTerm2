import  week6_grpb_proj2b_nlp
import pandas as pd

text3 = '    Jack and  jill have made a delicious,dish.Then they started to play some12 game! and jill has attahacd# [a] photo frame to the straight9 wall and swung on sea-saw. She was very happy. After the game, they both went to central London to enjoy some fast food.'


obj = week6_grpb_proj2b_nlp.Text_preprocessor()
# print("N Gram tokenization:")
# print(obj.ngram_tokenization(text3, 2))

a=[]
b=[]
with open('SMSSpamCollection.txt','r') as f:
    l=f.readlines()
    for j in l:
        # append label in a (that is either spam or ham )
        a.append(j.split('\t')[0])
        # actual email in b
        b.append(j.split('\t')[1])

# convert to pandas  dataframe
d = {'label':a,'document':b}
df = pd.DataFrame(d)
print(df.head())


from sklearn.model_selection import train_test_split
# '''Controls the shuffling applied to the data before applying the split.
# Pass an int for reproducible output across multiple function calls'''
training_data, testing_data = train_test_split(df, test_size=0.2, random_state=25)
print("training_data\n------------------\n",training_data)

print("training_data.shape\n------------------\n",training_data.shape)

training_data_clean = (
#     # remove_special_character removes number email and special character
    training_data.assign(clean_document = lambda x:[obj.remove_special_characters(text) for text in x.document])
#     # Tokenize word
    .assign(word_token = lambda x:[obj.tokenize(text) for text in x.clean_document])
#     # remove stop words
     .assign(stops= lambda x:[obj.removal_stop_words(text) for text in x.word_token])
#     # lemmitization
     .assign(stemorlem= lambda x:[obj.stem_or_lem(text,'stemm') for text in x.stops])
#      # # input to sklearn
    .assign(document_to_sklearn= lambda x: [" ".join(map(str,list_of_words)) for list_of_words in x.stemorlem ])
    )

print("training_data_clean\n------------------\n",training_data_clean)

# Feature Extraction
# import sklearn
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features = 50)
X = vectorizer.fit_transform([i for i in training_data_clean['document_to_sklearn']])
df_bow_sklearn = pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())
df_bow_sklearn['label'] = training_data_clean['label']
print("df_bow_sklearn\n------------------\n",df_bow_sklearn)


# # Modeling
from pycaret.classification import *

s = setup(data = df_bow_sklearn, target='label',
          numeric_features=vectorizer.get_feature_names(),
          session_id=123,verbose=False,silent=True)

m = create_model('nb')
print("m",m)
com  = compare_models(sort='F1')
print("com",com)




