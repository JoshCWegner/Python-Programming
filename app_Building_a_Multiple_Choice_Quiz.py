from python.Question import Question

quiz_question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

answers_for_quiz_questions = [
    Question(quiz_question_prompts[0], "a"),
    Question(quiz_question_prompts[1], "c"),
    Question(quiz_question_prompts[2], "b"),
]

def run_test(answer_for_quiz_questions):
    quiz_score = 0
    for question in answer_for_quiz_questions:
        answer = input(question.prompt)
        if answer == question.answer:
            quiz_score += 1
    if quiz_score == 3:
        print("=== YOU GOT ALL OF THE ANSWERS CORRECT===")
    else:
        print("You got " + str(quiz_score) + " out of " + str(len(answers_for_quiz_questions)) + " correct!")

run_test(answers_for_quiz_questions)