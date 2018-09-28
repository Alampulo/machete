'''
The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers" array and contains student's answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

If the score < 0, return 0.

'''


def check_exam(arr1,arr2):

    total = 0

    for i,results in enumerate(arr2):

        if results == arr1[i]:
            total += 4
        elif results!='':
            total-=1
    if total < 0:
        return 0
    return total
