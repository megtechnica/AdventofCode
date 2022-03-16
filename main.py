from program_data import sonar_output
import copy

sonar_output = copy.copy(sonar_output)

def depth_scan(sonar_output):
  numbers = [int(line) for line in sonar_output.splitlines()]

  count = 0

  previous = numbers[0]

  for num in numbers[1:]:
    if num > previous:
      count += 1
    previous = num

  return count
  
def sliding_window(sonar_output):
  # don't repeat yourself except right here
  numbers = [int(line) for line in sonar_output.splitlines()] 
  count = sum(numbers[i] > numbers[i - 3]
              for i in range(3, len(numbers)))
  return count

print(depth_scan(sonar_output))

print(sliding_window(sonar_output))
