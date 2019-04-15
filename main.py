# read lyrics data from file
# pass data into various threads, each computing feature data then storing that data into a feature data file
# take the feature data file and pass into word2vec model to get word embeddings


import threading
import logging

# # feature files
import lengthOfDocument


# list of features that need to be computed

list_of_feature_functions = [length_of_document]

def main():
	
	print("Read Lyrics from File")
	
	threads = []
	
	for feature in features:
		print("Spawning Thread for {}".format(feature))
		t = threading.Thread(target=feature)
		
	
	
	# join on all the features being used to compute the word embeddings



if __name__ == "__main__":
	main()