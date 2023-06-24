# This script removes the unnecessary '\n' in the original
# file, so that the translator service can work properly
# It produces a new file ready for translation

# open and read the original file
original_file = open("subtitles_original.srt","r")
try:
    content = original_file.read()
finally:
    original_file.close()

print("------ Successfully read the original file.")

# split the content into chunks by timestamps
content = content.split("\n\n")

# check if everything works as expected
# print(len(content))
# for i in range(3):
#     print(content[i])

# for the translation to work properly, we need to 
# remove all '\n' except for the first two. We do 
# this by replace the first two with a placeholder
# and at last replace the placeholder back
for i in range(len(content)):
    content[i]= content[i].replace("\n", "placehd", 2)

for i in range(len(content)):
    content[i]= content[i].replace("\n", " ")

for i in range(len(content)):
    content[i]= content[i].replace("placehd", "\n", 2)

for i in range(len(content)-1):
    content[i]= content[i] + "\n\n"

# check if everything works as expected
# for i in range(3):
#     print(content[i])

print("------ Successfully stripped the extra newlines.")

# write to a new file
preprocessed_file = open("subtitles_preprocessed.txt", "w")
try:
    preprocessed_file.writelines(content)
finally:
    preprocessed_file.close()

print("------ Successfully created and wrote to a new file.")