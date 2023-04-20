import json
import pickle
import random
from collections import defaultdict
from email.policy import default

if __name__ == "__main__":
    
    train_review_file  = './raw/graphrec.train.ratings'
    test_review_file  = './raw/graphrec.test.ratings'
    user_links_file = './raw/user.links'
    
    
    history_u_lists = defaultdict(list)
    history_ur_lists = defaultdict(list)
    history_v_lists = defaultdict(list)
    history_vr_lists = defaultdict(list)
    social_adj_lists = defaultdict(list)
    test_r = []
    test_u = []
    test_v = []
    train_r = []
    train_u = []
    train_v = []
    ratings_list = {
                    0:0,
                    1:1,
                    2:2,
                    3:3,
                    4:4,
                    5:5
                    }

    with open(train_review_file, "r") as f:
        for line in f:
            data = [int(x) for x in line.split(",")]
            u, v, r = data[0], data[1], data[2]
            history_u_lists[u].append(v)
            history_ur_lists[u].append(r)
            
            history_v_lists[v].append(u)
            history_vr_lists[v].append(r)
            
            train_u.append(u)
            train_v.append(v)
            train_r.append(r)
            
    
    with open(test_review_file, "r") as f:
        for line in f:
            data = [int(x) for x in line.split(",")]
            u, v, r = data[0], data[1], data[2]
            
            test_u.append(u)
            test_v.append(v)
            test_r.append(r)
        
    with open(user_links_file, "r") as f:
        for line in f:
            data = [int(x) for x in line.split(",")]
            u, v, s = data[0], data[1], data[2]
            social_adj_lists[u].append(v)
            
    
    with open('./data/yelp.pickle', 'wb') as f:
        pickle.dump([history_u_lists, history_ur_lists, history_v_lists, history_vr_lists, train_u, train_v, train_r, test_u, test_v, test_r, social_adj_lists, ratings_list], f, protocol=pickle.HIGHEST_PROTOCOL)

                   
    