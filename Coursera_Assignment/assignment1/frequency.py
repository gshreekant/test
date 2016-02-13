# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:03:16 2016

@author: shreez
"""

import sys
import json

def lines(fp):
    all_lines=fp.readlines() 
    print len(all_lines)
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
    w_list = []
    new_sentiment_scores = {}
    for word in l_json:      
        if word in sentiment_scores:
            sum_sentiment = sum_sentiment + sentiment_scores[word]
        else:
            w_list.append(word)            
    if sum_sentiment < 0:
        temp_score = -1
    elif sum_sentiment == 0:
        temp_score = 0
    else:
        temp_score = 1            
    for w in w_list:
        new_sentiment_scores[w] = int(temp_score)
            
    return new_sentiment_scores

def main():
    tweet_file = open(sys.argv[2], 'r+')
    tf_al = lines(tweet_file)
    l_score = []
    p_idx = 10
    idx   = 0
    ii = 1
    for line in tf_al:
        line_json = json.loads(line)
        if 'text' in line_json:
            score = calc_new_score(line_json, sf_al)
            ii = ii + 1
        else:
            score = 0
                
        l_score.append(score)
        print score
        idx = idx + 1
        if idx == p_idx:
            print line_json
            print score

    sent_file.close()
    tweet_file.close()
    print len(l_score)
    print ii
    

if __name__ == '__main__':
    main()
