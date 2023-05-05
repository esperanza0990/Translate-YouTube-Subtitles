#!/bin/bash

# This script takes a YouTube link, downloads its subtitle file,
# converts it to srt format(if necessary), translates it using
# Microsoft Azure Translator, and produces a translated subtitle
# file and a combined subtitle file with two languages.

# Prerequisite: you have run 'az login' to login to Azure before running this script
# you also need to have the correct role assigned for your Azure user

echo "---- Starts creating subtitle translation"

# variables
youtube_link=$1

# generate SAS token for the source and target file containers in Azure, you need to have container public access level set
source_container_sas_token=$(az storage container generate-sas --account-name my-storage-account-name --as-user --auth-mode login --expiry 2023-05-06 --name my-source-container-name --permissions lr)
target_container_sas_token=$(az storage container generate-sas --account-name my-storage-account-name --as-user --auth-mode login --expiry 2023-05-06 --name my-target-container-name --permissions lw)

# download the English subtitle file using youtube-dl, convert it to srt.
echo "---- Starts downloading English subtitle file from: " $youtube_link
youtube-dl --convert-subs srt --write-sub --sub-lang en --skip-download -o sub $youtube_link

# youtube-dl --convert-subs currently has a bug, it does not convert with the
# --skip-download flag, so we need to convert it from vtt to srt using ffmpeg.
ffmpeg -i sub.en.vtt subtitles_original.srt

# rename the srt file to txt format to use in Azure translator
mv subtitles_original.srt subtitles_original.txt

# remove trash
rm sub.en.vtt

# run the preprocessing python script, so that Azure Translator can work with it
python3 preprocessing_strip_newlines.py

# upload the preprocessed file to Azure Blob Storage container, using Azure cli
az storage blob upload --account-name my-storage-account-name --container-name my-source-container-name --name subtitles_preprocessed.txt --file subtitles_preprocessed.txt

# start translation
go run translate-subtitles.go $source_container_sas_token $target_container_sas_token

# wait for the translated document is written to the target container, this takes time
echo "---- wait for 40 seconds for the translated document to be ready"
sleep 40

# download the translated subtitle file from the target container
az storage blob download --account-name my-storage-account-name --container-name my-target-container-name --name subtitles_preprocessed.txt --file subtitles_translated.txt

# run the postprocessing python script, to produce a combined srt file containing two languages
python3 postprocessing_combine_languages.py

# other commands that may be useful: check file existence in Azure and use a while loop
# az storage blob exists --account-name my-storage-account-name --container-name my-target-container-name --name subtitles_preprocessed.txt | jq '.exists'

# while [ condition ]
# do
#    command1
#    command2
#    command3
# done