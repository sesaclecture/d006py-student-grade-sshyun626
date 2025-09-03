#!/usr/bin/env python
import sys
import csv


def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:]
    return student_scores, header[1:]


def subject_average(student_scores: dict, subjects: list):

    num_students = len(student_scores)
    subject_totals = [0] * len(subjects)

    # 학생별 점수 합산
    for scores in student_scores.values():
        for i, score in enumerate(scores):
            subject_totals[i] += int(score)

    # 평균 계산
    subject_avgs = {
        subject: subject_totals[i] / num_students
        for i, subject in enumerate(subjects)
    }

    return subject_avgs


def student_average(student_scores: dict):
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """
    student_avgs = []

    for name, scores in student_scores.items():
        avg = sum(map(int, scores)) / len(scores)
        student_avgs.append((name, avg))

    # 평균 점수 기준 내림차순 정렬
    student_avgs.sort(key=lambda x: x[1], reverse=True)

    return student_avgs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <csv_file>")
        sys.exit()

    student_scores, subjects = load_from_csv(sys.argv[1])
    sub_avg = subject_average(student_scores, subjects)
    stud_avg = student_average(student_scores)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")

