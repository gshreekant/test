import sys
import json

def lines(fp):
    all_lines=fp.readlines() 
    return all_lines
    
def create_dict(sf_al):
    afinnfile = sf_al
    sentiment_scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sentiment_scores[term] = int(score)  # Convert the score to an integer.
    return sentiment_scores
    
    
def calc_score(l_json, sf_al):
    sentiment_scores = create_dict(sf_al)
    sum_sentiment = 0
    for word in l_json:  
        if word in sentiment_scores:
            sum_sentiment = sum_sentiment + sentiment_scores[word]
    return sum_sentiment

def main():
    sent_file = open(sys.argv[1], 'r+')
    tweet_file = open(sys.argv[2], 'r+')
    sf_al = lines(sent_file)
    tf_al = lines(tweet_file)
    l_score = []
    for line in tf_al:
        line_json = json.loads(line)
        if 'text' in line_json:
            score = calc_score(line_json, sf_al)
            l_score.append(score)
            print score
 
    sent_file.close()
    tweet_file.close()
    

if __name__ == '__main__':
    main()
