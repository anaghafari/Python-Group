import random

with open('input.txt', 'r') as input_file, open('output.txt','a') as output_file:
  questions = input_file.readlines()
  question = random.choice(questions)
  print(question)
  answer = input('Your answer:')
  output_file.write(question)
  output_file.write(answer)
  output_file.write('\n')