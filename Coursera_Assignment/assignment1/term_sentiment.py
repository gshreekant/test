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
    
    
def calc_new_score(l_json, sf_al):
    sentiment_scores = create_dict(sf_al)
    sum_sentiment = 0
    new_word_list = []
    new_sentiment_scores = {}
    for word in l_json:      
        if word in sentiment_scores:
            sum_sentiment = sum_sentiment + sentiment_scores[word]
        else:
            print word
            new_word_list.append(word)            
    if sum_sentiment < 0:
        temp_score = -1
    elif sum_sentiment == 0:
        temp_score = 0
    else:
        temp_score = 1            
    for w in new_word_list:
        new_sentiment_scores[w] = int(temp_score)
            
    return new_sentiment_scores

def main():
    sent_file  = open(sys.argv[1], 'r+')
    tweet_file = open(sys.argv[2], 'r+')
    sf_al = lines(sent_file)
    tf_al = lines(tweet_file)
    new_dic = {}
    new_sentiment = {}
    idx = 0
    p_idx = 5
    for line in tf_al:
        line_json = json.loads(line)
        new_sentiment = {}
        idx = idx + 1
        if 'text' in line_json:
            new_sentiment = calc_new_score(line_json, sf_al)
            if idx == p_idx:
                print p_idx
                for (k,v) in new_sentiment:
                    print '%s %d' %(k, v)
        
#        for word in new_sentiment:
#            if not word in new_dic:
#                print '%s %d' %(word, new_sentiment[word])
                
        new_dic.update(new_sentiment)

    sent_file.close()
    tweet_file.close()
    

if __name__ == '__main__':
    main()
