import codecs
from pathlib import Path
import pickle
from nltk.stem.snowball import EnglishStemmer
from core.index_parser import Index
from utils.helpers import COLORS, show_text

# documents_path = Path("collection-tp")
# with open(documents_path / 'antidict.txt') as stopwords_stream:
# 	stopwords = stopwords_stream.read().splitlines()
# index = Index(stemmer=EnglishStemmer(), stopwords=stopwords)
# index.build_index(documents_path / "collection.lst", documents_path)
# index.to_json("index3.json")
# index.to_pickle("index.pckl")
# index3 = Index(pickled_index_file="index.pckl")
# print(index3.index)


def show_intro():
	print(COLORS.GREEN)


def main():
	show_intro()


if __name__ == '__main__':
	main()