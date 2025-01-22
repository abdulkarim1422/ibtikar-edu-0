from app.initializers import temp_data
from app.services.LLM import unicall_llm
import random
import json

def run_next_question(llm_type="gemini", student_grade="1", subject=None, subject_topics=[], completed_questions=[], false_questions=[]):
    user_prompt = f"""
    Sınıf: {student_grade}. Sınıf
    Ders: {subject}
    Konular: {subject_topics}
    """
    print("Sınıf: ", student_grade)
    print("Ders: ", subject)
    q = unicall_llm.unicall(llm_type=llm_type, system_prompt=temp_data.system_prompt, user_prompt=user_prompt)
    print(q)
    q = q.replace("json", "")
    q = q.replace("```", "")
    if __name__ == "__main__":
        print(q)
    try:
        q = json.loads(q)
    except:
        print("Sorun oluştu. Tekrar deneyeceğiz...")
        return run_next_question()
    print(q["soru"])
    print("A: ", q["A"])
    print("B: ", q["B"])
    print("C: ", q["C"])
    print("D: ", q["D"])
    print("E: ", q["E"])

    student_input = input("Cevap (A/B/C/D/E): ")
    if student_input.lower() == q["doğru seçenek"].lower():
        completed_questions.append([student_grade, subject, q])
        return True
    else:
        correction = unicall_llm.unicall(llm_type=llm_type, system_prompt=f"in the following question, the student answered {student_input}, correct it and explain", user_prompt=q)
        false_questions.append([student_grade, subject, (q["soru"], q[q["doğru seçenek"]], f"your answer was: {q[student_input.upper()]}"), correction])
        print(f"True Answer: {q[q["doğru seçenek"]]}\n", correction)
        return False
    
def zero_exam_loop():
    
    max_grade = 1
    completed_subjects = []
    completed_questions = []
    false_questions = []

    while True:
        available_subjects = []
        for key in temp_data.all_all:
            if int(key) <= max_grade:
                for sub_key in temp_data.all_all[key]:
                    if (key, sub_key) not in completed_subjects and all(sub_key != x for _,x in available_subjects):
                        available_subjects.append(((key), (sub_key)))
        print("available_subjects:", available_subjects)
        student_grade, subject = random.choice(available_subjects)
        subject_topics = temp_data.all_all[str(student_grade)][subject]
        test = run_next_question(llm_type="gemini", student_grade=student_grade, subject=subject, subject_topics=subject_topics, completed_questions=completed_questions, false_questions=false_questions)
        if test == True:
            print("Doğru")
            if int(student_grade) >= max_grade and max_grade <= 12:
                max_grade += 1
            completed_subjects.append(((student_grade), (subject)))
        if test == False:
            print("Yanlış")

        print("max_grade:", max_grade)
        print("Completed Subjects:", completed_subjects)
        print("completed_questions:", completed_questions)
        print("false_questions:", false_questions)
