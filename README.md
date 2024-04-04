# Waqq.ly cloud-based Web App

## A functioning prototype that allows users to register pets, and to register dog walkers

This README file will guide you through the steps on how to setup the Waqq.ly cloud-based Web App within Microsoft Azure.

## Prerequisites

* [GitHub account](https://github.com/)
* [Azure account](https://portal.azure.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/downloads)
* [Python 3.11 (or below) Interpreter](https://www.python.org/downloads/)
* [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) 
* [Azure Static Web Apps extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps)
* [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
* [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Azure Databases extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-cosmosdb)
* [GitHub Actions](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions)


## Setup Project

1.	Navigate to https://github.com and sign into your account.
2.	Open Visual Studio Code and ensure that you have no projects currently open.
3.	Ensure you are signed into Azure within Visual Studio Code.
4.	Ensure you are signed into GitHub within Visual Studio Code.
5.	Within Visual Studio Code, open Explorer > Open Folder > Create a new folder called “Waqqly” in a location of your choice > Select Folder.
6.	Within Explorer in Visual Studio Code, right click within the Waqqly folder > New Folder > Name it “src”.
7.	Right click the src folder > New File > Name it “index.html”.
8.	Open any web browser and navigate to https://github.com/nbarron24/Waqqly.
9.	Open the src Folder > Open index.html > Copy the contents of the index.html file.
10.	Open Visual Studio Code > Paste the contents of your clipboard into the index.html file.

## Setup Static Web App

1.	Select Azure (A) within Visual Studio Code.
2.	Hover your cursor within Resources and select the “+” button (Create Resource…) > Type and Select “Create Static Web App” > Create > Leave commit message as default > Use the following details:
    * Static Web App Name: Waqqly
    * GitHub Repository Name: Waqqly
    * Region: West Europe
    * Build: Custom
    * Application Code Location: /src
    * Build Location: /src
3.	Open Explorer within Visual Studio Code > Expand Waqqly > Expland .github > Copy the app_location and api_location lines (should be lines 31 and 32) > Paste both before the line, action: “Close” (should be the last line).
4.	Go to File > Save.
5.	Go to Source Control > Commit > Select Save All & Commit Changes > Sync Changes.


## Setup Azure Functions

1.	Within Visual Studio Code, go to View > Command Palette > Type and select Azure Static Web Apps: Create HTTP Function > Use the following details:
    * Language: Python
    * Programming Model: Model V2
    * Python Interpreter: Select your Python interpreter (part of Prerequisites)
    * Function Name: registerDog
    * Authorisation: ANONYMOUS
2.	Open any web browser and navigate to https://github.com/nbarron24/Waqqly.
3.	Open the api Folder > Open function_app.py > Copy the contents of the function_app.py file.
4.	Open Visual Studio Code > Open Explorer > Expand Waqqly > Expand api > Paste the contents of your clipboard into the function_app.py file.
5.	Select Azure (A) within Visual Studio Code.
6.	Hover your cursor within Resources and select the “+” button (Create Resource…) > Type and Select “Create Function App in Azure” > Use the following details:
    * Name: Waqqly-Functions
    * Runtime Stack: Python 3.11
    * Location: UK South

## Setup Cosmos DB

1.	Select Azure (A) within Visual Studio Code.
2.	Hover your cursor within Resources and select the “+” button (Create Resource…) > Type and Select “Create Database Server” > Use the following details:
    * Azure Database Server: Core (SQL)
    * Account Name: waqqly-db
    * Capacity Model: Serverless
    * Resource Group: waqqlyfunctions
3.	Under Resources, expand your subscription > Expand Azure Cosmos DB > Right click waqqly-db > Select Create Database > Use the following details:
    * Database Name: waqqly_database
    * Collection: waqqly_container
    * Partition Key: /id
4.	Under Resources, right click waqqly-db > Copy connection string.
5.	Go to View > Command Palette > Type and select Azure Functions: Add New Setting > select Waqqly-Functions > Use the following details:
App Setting Name: CosmosDbConnectionSetting
Value: Paste Connection String
6.	Go to View > Command Palette > Type and select Azure Functions: Download Remote Settings > Select Waqqly-Functions > Select Yes to all.

## Get Azure Functions URL

1.	Within Visual Studio Code, go to Run > Start Debugging > Select Connect Storage Account as Waqqlyfunctions (if required) > Wait for the terminal to show the two functions.
2.	Select Azure (A) within Visual Studio Code.
3.	Under Resources, expand your subscription > Expand Function App > Right click Waqqly-Functions > Deploy to Function App > Deploy.
4.	Under Resources, expand Functions under Waqqly-Functions > Right Click registerDog > Copy Function Url.
5.	Open Explorer within Visual Studio Code > Expand Waqqly > Expand src > Select index.html > Find the form for registering a dog and remove the URL after the word action but keep the speech marks (should be line 20) > Paste the Copied Function URL in between the speech marks (“”).
6.	Select Azure (A) within Visual Studio Code.
7.	Under Resources, expand Functions under Waqqly-Functions > Right Click registerWalker > Copy Function Url.
8.	Open Explorer within Visual Studio Code > Expand Waqqly > Expand src > Select index.html > Find the form for registering a walker and remove the URL after the word action but keep the speech marks (should be line 35) > Paste the Copied Function URL in between the speech marks (“”).
9.	Go to File > Save.
10.	Go to Source Control > Commit > Sync Changes.

## Accessing the Waqq.ly cloud-based Web App

1.	Access your GitHub Repository via the web browser and ensure that the last commit was successful (indicated by a green tick).
2.	Select Azure (A) within Visual Studio Code.
3.	Under Resources, expand your subscription > Expand Static Web Apps > Right click Waqqly > Select Browse Site > Open.
4.	Congratulations, the Waqq.ly cloud-based Web App is up and running.
