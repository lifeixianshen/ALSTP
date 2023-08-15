# choose dataset name
dataset = 'toys'

# paths
main_path = '/home/share/guoyangyang/amazon/'
stop_file = './stopwords.txt'

processed_path = './processed/'

full_path = f'{processed_path}{dataset}_full.csv'
train_path = f'{processed_path}{dataset}_train.csv'
test_path = f'{processed_path}{dataset}_test.csv'

asin_sample_path = f'{processed_path}{dataset}_asin_sample.json'
user_bought_path = f'{processed_path}{dataset}_user_bought.json'

doc2model_path = f'{processed_path}{dataset}_doc2model'
query_path = f'{processed_path}{dataset}_query.json'

# embedding size
embed_size = 512
