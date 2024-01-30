# In read_file, I get the contents of the file which I push into a list, after removing the newline.
def read_file(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
    return content


# decode_message is the main function.
def decode_message(file_path):
    lines = read_file(file_path)

    # We sort the lines in ascending order of number.
    lines.sort(key=lambda x: int(x.split()[0]))

    step = 1
    result = []
    subsets = 0
    
    for line in lines:
        subsets += 1
        # if the number of values ​​present in the current step is reached
        # then we save the content of the last value and we start on a new step
        if subsets >= step:
          step += 1
          # we create the new step of our staircase
          subsets = 0
          # we add the content of our line to the final text
          result.append(line)

    return "\n".join(result)
    
print(decode_message("./test.txt"))
