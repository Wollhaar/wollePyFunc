exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
  return score >= 70

status = list(map(is_passing, exam_scores))

print(status)


numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))

print(doubled)