from sys import base_prefix


class Text_preprocessor:
    """
       A class to preprocess text for NLP Application.

       ...

       Attributes
       ----------
       spec_filtered : list
         list with special character removed
       rm_stopwrds : list
         list with stopwords removed
       clean : list
         list after all text preprocessing
       index_word : dict
         dict of indexed words
       bag_of_words : df
         list of words after preprocessing document


       Methods
       -------
       expand_contraction(text=""):
           returns the expanded text.

       remove_special_characters(text=""):
           returns text with removed emailaddress, special characters and numbers

       tokenize(text=")
           returns list of words from text

       removal_stop_words(token=[],language='english')
           stop words are derived from  nltk.corpus
           returns the list with removed stopwords for english language

       stem_or_lem(token=[],method="stemm")
           return the list after lemmitization or stemmization depending upon 
           method argument

       preprocessed_text(text="")
           returns list of words after performing
           contaraction, removal of special characters, tokenization, removal of
           stop word, stemmization and lemmitization

       bow(document)
           returns bag of words for a document(sentence)


       get_word_dict
           returns key value pair for words in document

       computeTF
           return dict of computed TF for documents

       computeTFIDF
           returns dict of IDFS for words in corpus

       computeTFIDF
           returns dict of computed TFIDF for words in documents

       dict_to_df
           returns pandas dataframe representing TFIDS of  list of documents of document
       """

    def __init__(self):
        self.spec_filtered = []
        self.rm_stopwrds = []
        self.clean = []
        self.index_word = {}
        self.bag_of_words = []
        self.corpus_words = []
        self.clean_document_list = []

    def expand_contraction(self, text: str) -> str:
        '''
        Expands the words in text with contractions module.

            Parameters
            ----------
            text : str,
                text to be expanded

            Returns
            -------
            text with expanded words 
        '''
        # create an empty list
        expanded_words = []
        for word in text.split():
            # using contractions.fix to expand the shotened words and removes extra spaces
            expanded_words.append(contractions.fix(word))
        expanded_text = ' '.join(expanded_words)
        return expanded_text.lower()

    def remove_special_characters(self, text: str) -> str:
        '''
      Removes the email, special character and numbers from text.

          Special character includes ! @ # $ & * () + - [].

          Parameters
          ----------
          text : str
              String containing special character

          Returns
          -------
          String without email, special character and numbers
      '''
        # remove email if any
        txt_email = re.compile(r'[A-Za-z0-9]*@[A-Za-z]*\.com')
        cln_txt = txt_email.sub('email', text)
        # remove special character and number if any
        self.spec_filtered = re.sub('[^A-Za-z]+', ' ', cln_txt)
        return self.spec_filtered

    def tokenize(self, text: str) -> list:
        '''
          Tokenize the text  to form list.
             Use nltk.word_tokenize.

             Parameters
             ----------
             text : str, 
             text to  tokenize

             Returns
             -------
             list of tokenized words
         '''

        nltk_tokens = nltk.word_tokenize(text)
        return nltk_tokens

    def removal_stop_words(self, tokens: list, language: str = 'english') -> list:
        '''
         Removes the stop words from list.

             Use stopwords from nltk.corpus.

             Parameters
             ----------
             token : list
                 words token
             language : str, optional 
             Language of the words (default is english) 

             Returns
             -------
             list of words without stop words
         '''
        stopword_list = nltk.corpus.stopwords.words(language)
        self.rm_stopwrds = [
            word for word in tokens if not word in stopword_list]
        return self.rm_stopwrds

    def stem_or_lem(self, tokens: list, method: str) -> list:
        '''
         Perform Stemming or lemmatization.
         If the argument method is 'stemm' then performs stemmization, performs
         lemmitization if 'lemm' and return tokens for mismatched strings
         PorterStemmer  from nltk for stemming
         WordNetLemmatizer from nltk for lemmatization

             Parameters
             ----------
             tokens : list
                list of tokenized words

             Returns
             -------
             return words after Stemming or Lemmatization
         '''
        # instance of PorterStemmer
        ps = PorterStemmer()
        stemmed = []
        lemmed = []
        if method == 'stemm':
            for w in tokens:
                rootWord = ps.stem(w)
                stemmed.append(rootWord)
            return stemmed
        elif method == 'lemm':
            wordnet_lemmatizer = WordNetLemmatizer()
            for w in tokens:
                lemm = wordnet_lemmatizer.lemmatize(w)
                lemmed.append(lemm)
            return lemmed
        else:
            return tokens

    def preprocessed_text(self, text: str) -> list:
        '''
        Perfoms all the operation of text preprocessing.


            Parameters
            ----------
            text : str, 
                string to be preprocessed
            Returns
            -------
            returns list of words after performing
            contaraction, removal of special characters, tokenization, removal of
            stop word, stemmization and lemmitization

        '''
        exp_text = self.expand_contraction(text)
        prune_special = self.remove_special_characters(exp_text)
        tokenize_words = self.tokenize(prune_special)
        remove_stopwords = self.removal_stop_words(tokenize_words, 'english')
        # stemmed =self.stem_or_lem(remove_stopwords,'stemm')
        self.clean = self.stem_or_lem(remove_stopwords, 'lemm')
        return self.clean

    def get_word_dict(self, dirty_text, document):
        '''
         Returns the dict of words after achieved after cleaning

           Parameter
           ---------
           dirty_text : list 
             list of documents before preprocessing

           document : list 
              list of string [raw_document]

           Returns
           -------
             (key ,value) 
             Key : word
             value : frequency of words in document
        '''

       #  all_words = self.get_corpus_words(text)
        flatten_list = [item for sublist in self.pre_prep(
            dirty_text) for item in sublist]
        all_words = list(set(flatten_list))
        clean_document = self.preprocessed_text(document)

       #  words dictionary with value 0
        wordDict = dict.fromkeys(all_words, 0)
        for word in clean_document:
            # count occurence of each words
            if word in wordDict:
                wordDict[word] += 1
        return wordDict

    def pre_prep(self, dirty_text: list) -> list:
        '''
          Returns the list  of documents of documents

            Parameter
            ---------
            dirty_text : list 
              list of documents before preprocessing


            Returns
            -------
              list of clean documents of clean document
         '''
        for document in dirty_text:
            self.clean_document_list.append(self.preprocessed_text((document)))
        return self.clean_document_list

    def bow(self, dirty_text: list) -> list:
        '''
         Returns the bag of words in pandas dataframe format

           Parameter
           ---------
           dirty_text : list 
             list of documents of raw_documents


           Returns
           -------
             bag of words in pandas Df
        '''

        flatten_list = [item for sublist in self.pre_prep(
            dirty_text) for item in sublist]
        unique_words = list(set(flatten_list))
        #  indexing the words from corpus
        # first parameter  into keys and second is value(index)
        indexed_words = dict(zip(unique_words, range(len(unique_words))))
        bow_qrr = []
        for document in self.clean_document_list:
            #  create numpy array of of length of corpus
            empty_arr = np.zeros(len(unique_words))
            #  count the occurence of the each words
            for word in document:
                empty_arr[indexed_words[word]] += 1
            bow_qrr.append(empty_arr)
            #  convert array to dataframe
        df = pd.DataFrame(bow_qrr, columns=unique_words)
        return df

    def computeTF(self, dirty_text: list, document) -> dict:
        '''
        Computes TF for each word in  document

        Parameter
        ---------
          dirty_text : list documents of document

            document: list
             List of strings(raw_document)

        Returns
        --------
          dict
          key : word
          value : term frequency of the word

        '''
        tfDict = {}
        len_sntn = len(self.preprocessed_text(document))
        word_dict = self.get_word_dict(dirty_text, document)
        for word, count in word_dict.items():
            # term frequency for words in a sentence
            tfDict[word] = count/float(len_sntn)
        return tfDict

    def computeIDF(self, dirty_text: list) -> dict:
        '''
          Computes IDFs for all word in doclist

          Parameter
          ---------
            dirty_text : list  
              list of pre-processed documents

          Returns
          --------
            dict
            key : word
            value : IDFS for each word

          '''
        doc_list = []
        for doc in dirty_text:
            word_dict = self.get_word_dict(dirty_text, doc)
            doc_list.append(word_dict)

        idfDict = {}
        N = len(doc_list)
        # dict with all words with value 0(template)
        idfDict = dict.fromkeys(doc_list[0].keys(), 0)
        for doc in doc_list:
            for word, val in doc.items():
                if val > 0:
                    # increase the value if the word exist in doc
                    idfDict[word] += 1
        for word, val in idfDict.items():
            idfDict[word] = math.log10(N / float(val))
        return idfDict

    def computeTFIDF(self, tf, idfs) -> dict:
        '''
        Computes TFIDFs for all word in documents

          Parameter
          ---------
            tfBow : dict  
              Key: word
              value: tf of word in document
            idfs: dict
              key : Word
              value: idf of word in document list 


          Returns
          --------
            dict
            key : word
            value : TfIDFS for each word in document

        '''
        tfidf = {}
        for word, val in tf.items():
            tfidf[word] = val*idfs[word]
        return tfidf

    def dict_to_df(self, text) -> list:
        '''
        Performs all above operations to 
        Generates pandas dafarame

           Parameter
           ---------
             text : list of documents (corpus)  


           Returns
           --------
             Pandas dataframe
         '''
        arr = []
        idfs = self.computeIDF(text)
        for doc in text:
            tf = self.computeTF(text, doc)
            tfidf = self.computeTFIDF(tf, idfs)
            arr.append(tfidf)
        df = pd.DataFrame(arr)
        return df

    def pos_identification(self, text) -> list:
        '''
        identifies Part of speech in given text 

           Parameter
           ---------
             text : string   


           Returns
           --------
             list of tuple with identification

        '''
        return nltk.pos_tag(nltk.word_tokenize(self.remove_special_characters(text)))

    def name_entity_identification(self, text: str, lib='spacy') -> list:
        '''
        identifies name or entity of text in given text 

           Parameter
           ---------
             text : string   


           Returns
           --------
             list of tuple with identification

        '''
        #  use nltk for identification
        if lib == 'nltk':
            print("Using Nltk lib")
            for chunk in nltk.ne_chunk(self.pos_identification(text)):
                if hasattr(chunk, 'label'):
                    idntfy = ([(chunk.label(), chunk) for c in chunk])

            # use spacy for identification
        doc = nlp(obj.remove_special_characters(text))
        idntfy = ([(X.text, X.label_) for X in doc.ents])
        return ([(X.text, X.label_) for X in doc.ents])

    def ngram_tokenization(self, text, n=2) -> list:
        '''
        identifies name or entity of text in given text 

           Parameter
           ---------
             text : string   


           Returns
           --------
             list of tuple with identification

        '''
        n_grams = ngrams(nltk.word_tokenize(
            obj.remove_special_characters(text)), n)
        return [' '.join(grams) for grams in n_grams]


text2 = ['This is a good movie.',
         'It is a good movie, but you know good is relative.',
         'Movie is fun to watch.',
         'I had a good relaxing time.',
         'The whole cinema experience was good.',
         'This is a good cinema.']

text3 = '    Jack and  jill have made a delicious,dish.Then they started to play some12 game! and jill has attahacd# [a] photo frame to the straight9 wall and swung on sea-saw. She was very happy. After the game, they both went to central London to enjoy some fast food.'


obj = Text_preprocessor()


# print("BOW:")
# print(obj.bow(text2))

# print("TF for a sentence :")
# print(obj.computeTF(text2, text2[0]))

# print("IDFS:")
# print(obj.computeIDF(text2))

# print("TFIDFS:")
# print(obj.dict_to_df(text2))

# print("Cleaning:")
# print(obj.remove_special_characters(text3))

# print("POS Identification:")
# print(obj.pos_identification(text3))

# print("Name Entity identification:")
# print(obj.name_entity_identification(text3))

print("N Gram tokenization:")
obj.ngram_tokenization(text3, 2)
