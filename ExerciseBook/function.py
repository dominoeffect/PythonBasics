# def convert_to_numeric(score):
#     """
#     Convert the score to a numerical type.
#     """
#     converted_score = float(score)
    
#     return converted_score

# #print(convert_to_numeric(1))

# def sum_of_middle_three(score1,score2,score3,score4,score5):
#     """
#     Find the sum of the middle three numbers out of the five given.
#     """
#     sumnumber = (score1+score2+score3+score4+score5) - max(score1,score2,score3,score4,score5) - min(score1,score2,score3,score4,score5)
    
#     return sumnumber
    
# #print(sum_of_middle_three(1,2,3,4,5))

# def score_to_rating_string(score):
#     """
#     Convert the average score, which should be between 0 and 5, 
#     into a string rating.
#     """
#     if score < 0:
#     	rating = "Error"
#     elif 0 <= score < 1:
#         rating = "Terrible"
#     elif 1 <= score < 2:
#         rating = "Bad"
#     elif 2 <= score < 3:
#         rating = "OK"
#     elif 3 <= score < 4:
#         rating = "Good"
#     elif 4 <= score < 5:
#     	rating = "Excellent"
#     else:
#         rating = "Error"

#     return rating 

# def scores_to_rating(score1,score2,score3,score4,score5):
#     """
#     Turns five scores into a rating by averaging the
#     middle three of the five scores and assigning this average
#     to a written rating.
#     """
#     #STEP 1 convert scores to numbers
#     score1 = convert_to_numeric(score1)
#     score2 = convert_to_numeric(score2)
#     score3 = convert_to_numeric(score3)
#     score4 = convert_to_numeric(score4)
#     score5 = convert_to_numeric(score5)

#     #STEP 2 and STEP 3 find the average of the middle three scores
#     average_score =  sum_of_middle_three(score1,score2,score3,score4,score5)/3

#     #STEP 4 turn average score into a rating
#     rating = score_to_rating_string(average_score)

#     return rating

# print(scores_to_rating(1,4,4,4,5))




def convert_to_numeric(score):
    """
    Convert the score to a float.
    """
    converted_score = float(score)
    return converted_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum


def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5, 
    into a rating.
    """
    if av_score < 1:
        rating = "Terrible"
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Good"
    else:          #Using else at the end, every possible case gets caught
        rating = "Excellent"
    return rating


def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating






# 我们回顾一下创建 scores_to_rating() 函数时的步骤

# 1.收集函数的要求，包括输入和输出
# 2.首先将该过程分成简单的语言，而不是代码。
# 3.创建执行每个步骤的函数框架，包括尚未定义的帮助函数。
# 4.在这个阶段，调整步骤使编码更容易
# 5.创建帮助函数框架。
# 6.填写帮助函数的代码，测试其功能。
# 7.完成主函数的代码，调用每个帮助函数，并测试其功能。



