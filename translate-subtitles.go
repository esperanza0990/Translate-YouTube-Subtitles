// This file does the actual translation with Azure services.
// Reference: https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/how-to-guides/use-rest-api-programmatically?tabs=go
package main

import (
	"bytes"
	"fmt"
	"net/http"
	"os"
	"strings"
)

func main() {
	source_container_sas_token := os.Args[1]
	source_container_sas_token = strings.Trim(source_container_sas_token, "\"")
	target_container_sas_token := os.Args[2]
	target_container_sas_token = strings.Trim(target_container_sas_token, "\"")
	azure_translator_endpoint := "<copy-your-endpoint-from-the-azure-portal>"
	azure_translator_key := "<your-translator-key>"
	request_uri := azure_translator_endpoint + "/batches"
	request_method := "POST"

	json_content := fmt.Sprintf(`{
		"inputs": [
		   {
			  "source": {
				 "sourceUrl": "https://<my-storage-account>.blob.core.windows.net/<my-source-container>?%s",
				 "storageSource": "AzureBlob",
				 "language": "en"
			  },
			  "targets": [
				 {
					"targetUrl": "https://<my-storage-account>.blob.core.windows.net/<my-target-container>?%s",
					"storageSource": "AzureBlob",
					"category": "general",
					"language": "zh-Hans"
				 }
			  ]
		   }
		]
	 }
	`, source_container_sas_token, target_container_sas_token)

	var json_content_string = []byte(json_content)
	req, err := http.NewRequest(request_method, request_uri, bytes.NewBuffer(json_content_string))
	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Add("Ocp-Apim-Subscription-Key", azure_translator_key)
	req.Header.Add("Content-Type", "application/json")

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()
	fmt.Println("------ Response status:", res.Status)
	fmt.Println("------ Translation in progress, please wait and be patient")
}
