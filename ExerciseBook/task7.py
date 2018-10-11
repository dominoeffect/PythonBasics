def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= [None, None, None, None, None]
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[0]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print(check_answers([1,23,42,123,42],[1,23,42,11,32]))












def check_answers(my_answers,answers):
    #1 variable names are not easy to tell apart
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    #2 Code will only work if there are exactly five answers
    results= [None, None, None, None, None]
    #3 Repeated code would be better as a separate function
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    #4 if and elif could be clearer with if and else
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[0]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    #6 this function does several things in one long block
    count_correct = 0
    count_incorrect = 0
    for result in results:
    #7 The code counts both correct and incorrect answers.
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
    #8 The pass rate has been hard-coded into the function
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
1： 名称 my_answers 和 answers 非常相似，这有点混乱。为这些参数设置更好的名称，并将其定义放在文档字符串中以供参考。

2： 练习中的五个问题对运行代码至关重要。虽然这个约束不能阻止其正常运行，但如果将来我们有一个包括十个问题的练习，可以重复使用同样的代码就好了。

3： 此部分用于检查答案

    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[0]:
        results[1] = False
重复五次！使用一个单独的函数检查答案将更好。

4： 有几处使用 if 和 elif，但是 elif 子句中的布尔表达式只是 if 之后的内容。此种情况下，如果我们使用 if 和 else，该程序可正常运行，但是更容易阅读。

5： 没有解释代码作用的行内注释。

6： 该函数的作用不止一点 —— 检查每个答案，然后总计正确和错误答案的数量，然后输出一则消息。但至少应将某些作用分开。

7： 如果每个问题非对即错，而且我们知道有多少个问题，那么就不需要计数正确答案和错误答案的数量。也可以通过使用 sum 计数 results 中的正确答案，使代码更短。

8： 在通过练习的边缘中，正确答案的比例是硬编码的，也不需要。

完善该函数的方法很多！