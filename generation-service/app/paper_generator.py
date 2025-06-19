

def generate_unique_papers(questions, total_marks, num_papers):
    all_papers = []
    
    for _ in range(num_papers):
        selected = []
        current_sum = 0
        remaining_questions = questions[:]

        if not backtrack(remaining_questions, 0, selected, total_marks, current_sum):
            break  # Stop if we can't generate more papers

        all_papers.append(selected)
        questions = [q for q in questions if q not in selected]  # Remove used questions
    
    return all_papers


def backtrack(questions, index, selected, total_marks, current_sum):
    if current_sum == total_marks:
        return True  # Found a valid paper

    if current_sum > total_marks or index >= len(questions):
        return False  # Exceeded marks or no more questions left

    # Try including the current question
    selected.append(questions[index])
    if backtrack(questions, index + 1, selected, total_marks, current_sum + questions[index]["Marks"]):
        return True

    # Backtrack (remove the last added question)
    selected.pop()
    return backtrack(questions, index + 1, selected, total_marks, current_sum)