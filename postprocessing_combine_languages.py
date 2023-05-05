# This script combines the English subtitle file and the
# translated Chinese subtitle file, to generate a new srt
# file containing 2 languages. The generated file is ready
# to use in video.

# open and read the English subtitle file
english_file = open("subtitles_preprocessed.txt","r")
try:
    english_content = english_file.read()
finally:
    english_file.close()

print("------ Successfully read the English subtitle file.")

# open and read the Chinese subtitle file
chinese_file = open("subtitles_translated.txt","r")
try:
    chinese_content = chinese_file.read()
finally:
    chinese_file.close()

print("------ Successfully read the Chinese subtitle file.")

# split the contents into chunks by timestamps, remove the trailing '\n'
english_content = english_content.split("\n\n")
english_content = english_content[:len(english_content)-1]
chinese_content = chinese_content.split("\n\n")
chinese_content = chinese_content[:len(chinese_content)-1]

# the lengths of english_content and chinese_content should be equal
# print(len(english_content) == len(chinese_content))
# print(len(english_content))

combined_content = []
for i in range(len(english_content)):
    chinese_translation = chinese_content[i].split("\n")[2]
    combined_content.append(english_content[i] + "\n" + chinese_translation)

# the lengths of english_content and combined_content should be equal
# print(len(english_content) == len(combined_content))

for i in range(len(combined_content)):
    combined_content[i] = combined_content[i] + "\n\n"

# check if everything works as expected
# for i in range(3):
#     print(combined_content[i])

print("------ Successfully combined the English and Chinese subtitles.")

# write to a new file
postprocessed_file = open("subtitles_combined.srt", "w")
try:
    postprocessed_file.writelines(combined_content)
finally:
    postprocessed_file.close()

print("------ Successfully created and wrote the combined content to a new file.")