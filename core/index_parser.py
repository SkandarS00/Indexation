import codecs
from collections import defaultdict
import json
from pathlib import Path
import pickle
import nltk
from nltk.stem.snowball import _StandardStemmer
# from .exceptions import FileNotJsonError, SettingNotFoundError, SettingsFileNotFoundError


class Index:
	"""This is a python Index helper"""

	def __init__(
		self,
		stemmer: _StandardStemmer = None,
		stopwords=None,
		pickled_index_file=None
	):
		"""
		Args:
			tokenizer: For example: nltk.word_tokenize
			stemmer : For example: nltk.stem.snowball.EnglishStemmer()
			stopwords : _description_. 
		"""
		if pickled_index_file:
			with open(pickled_index_file, mode='rb') as iu:
				self.index = pickle.load(iu).index
		else:
			self.stemmer = stemmer
			self.index = defaultdict(list)
			self.stopwords = set(stopwords) if stopwords else set()
		

	@staticmethod
	def get_words(document_path) -> list:
		from nltk import word_tokenize
		with codecs.open(document_path, mode='r',
							encoding='UTF-8') as document:
			return word_tokenize(document.read())

	def build_index(
		self, file_points_to_docs: Path, absolute_path_for_doc_pointers
	):
		with open(file_points_to_docs, mode='r') as collection_stream:
			documents = collection_stream.read().splitlines()
			for document_path in documents:
				words_list = [
					t.lower() for t in Index.
					get_words(absolute_path_for_doc_pointers / document_path)
				]
				for word in words_list:
					if word in self.stopwords:
						continue
					if word in self.index.keys():
						self.index[self.stemmer.stem(word)
									].append(document_path)
					else:
						self.index[self.stemmer.stem(word)] = [
							document_path,
						]

	def lookup(self, word):
		"""
		Lookup a word in the index
		"""
		word = word.lower()
		if self.stemmer:
			word = self.stemmer.stem(word)

		return self.index.get(word)

	def add(self, document):
		"""
		Add a document string to the index
		"""
		for token in [t.lower() for t in nltk.word_tokenize(document)]:
			if token in self.stopwords:
				continue

			if self.stemmer:
				token = self.stemmer.stem(token)

			if self.__unique_id not in self.index[token]:
				self.index[token].append(self.__unique_id)

		self.documents[self.__unique_id] = document

	def to_pickle(self, pickle_filepath: str):
		with codecs.open(pickle_filepath, mode='wb') as pickle_filestream:
			import pickle
			pickle.dump(self, pickle_filestream)

	def to_json(self, json_filepath: str):
		with open(json_filepath, mode='w') as file_write_stream:
			json.dump(self.index, file_write_stream, indent=4, sort_keys=True)

	def add_to_setting(self, setting_key: str, value: str):
		setting = self.get_setting(setting_key)
		if isinstance(setting, list) and value not in setting:
			setting.append(value)

	def setting_exists(self, setting_key: str):
		return setting_key in self.settings.keys()
