from exercise import Exercise
from sheet import Sheet

exercise = Exercise()
sheet = Sheet()

answer = input("Tell me which exercise you did today? ").lower()

try:
    data = exercise.query_calories(query=answer)
except:
    raise Exception("Exercise class failed")
else:
    sheet.update_row(info=data)
