def top_students(scores , n):
    top_scores = dict(sorted(scores.items() , key= lambda x : x[1] , reverse = True))
    top_lst = list(top_scores)[:n]
    return top_lst

if __name__ == "__main__":
    scores = {"小明": 85, "小红": 92, "小刚": 78, "小丽": 95, "小军": 88}
    print(top_students(scores, 3))