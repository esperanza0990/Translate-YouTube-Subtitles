# Translate YouTube Subtitles

This is a bash script that downloads a subtitle file of a YouTube video, converts it to srt format, translates it and combines the two languages into one srt file. The scripts are easy to understand and modify. Uses `Azure Translator - Document Translation` service.

## To use: 

`bash RunMeWithYouTubeLink.sh "<youtube-video-link>"`

For example ([Crash Course Engineering EP03](https://www.youtube.com/watch?v=A1V-QQ5wFU4")): 

`bash RunMeWithYouTubeLink.sh "https://www.youtube.com/watch?v=A1V-QQ5wFU4"`

And then check for the `subtitles-combined.srt` file in the directory.

## Dependencies:
* youtube-dl: to download subtitles of YouTube video.
* ffmpeg: convert downloaded subtitles to srt format, if needed
* azure-cli: to use Azure Translator service

## Prerequisites(See Azure documentation for details):
* A Microsoft Azure account with an available subscription
* You have run `az login` on your terminal to login to Azure before executing the script `RunMeWithYouTubeLink.sh`
* In your Azure storage account used for translation, you are assigned the "Storage Blob Data Owner" role
* Your source and target containers inside your storage account have the Container public access level. 
* Make sure to have the correct permissions when generating the SAS token for your source (read & list) and target containers (write & list). See Azure documentation for details.
* You need to have your storage container sas tokens, Azure Translator key and enpoint written in the code. This is not safe. A better approach is to use Azure Key Vault and not explicitly writing out the credentials. But this repo is casual so whatever.

## References:
* [Azure Translator - Document Translation](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/overview)
* [Azure CLI - az storage container](https://learn.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest)
* [Azure CLI - az storage blob](https://learn.microsoft.com/en-us/cli/azure/storage/blob?view=azure-cli-latest)