def get_names(file_path):
    with open(file_path , mode="r") as names:
        invited_names = names.readlines()

    invited_names = [name.rstrip() for name in invited_names]
    return invited_names

#get list of names without new lines
names = get_names("Input/Names/invited_names.txt")

#get contents from sample letter
with open("Input/Letters/starting_letter.txt", mode="r") as content:
    content_for_letter = content.read()

#write the letters
for name in names:
    content = content_for_letter.replace("[name]", name)
    with open(f"Output/ReadyTosend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(content)