# QuizBrain Class Documentation

The `QuizBrain` class represents a quiz game engine that manages the flow of questions and user answers.

## Class Methods

### `__init__(self, q_list)`
Constructor method for initializing a `QuizBrain` object.

**Parameters:**
- `q_list` (list): A list of `Question` objects representing the questions in the quiz.

### `still_has_questions(self)`
Checks if there are still questions remaining in the quiz.

**Returns:**
- `bool`: `True` if there are still questions, `False` otherwise.

### `next_question(self)`
Displays the next question and prompts the user for an answer.

### `check_answer(self, user_answer, correct_answer)`
Compares the user's answer with the correct answer and updates the score accordingly.

**Parameters:**
- `user_answer` (str): The user's answer to the question.
- `correct_answer` (str): The correct answer to the question.

## Instance Attributes

- `question_number` (int): The current question number.
- `question_list` (list): A list of `Question` objects representing the questions in the quiz.
- `score` (int): The current score of the player.

