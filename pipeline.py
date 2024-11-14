import json
import requests
import pyfiglet
from colorama import Fore, Style

def ask_question_and_save_results():

    ascii_banner = pyfiglet.figlet_format("Ask Bruno")
    print(ascii_banner)

    #user input for the question and the file name
    question = input("Enter your question: ")
    file_name = input("Enter the file name (optional): ")
    output_format = input("Choose output format (txt, json, or both): ")

    #define Vectorshift API details
    url = "https://api.vectorshift.ai/api/pipelines/run"
    api_key = "sk_0LoqGm7LncV2pwF5oyJPB5hxAJFGN5miYChmj2wf1XorXhDL"

    headers = {
      "Api-Key": api_key
    }

    #Prepare the data payload with user input
    data = {
        "inputs": json.dumps({
            "input_1": question
        }),
    "pipeline_name": "MyCoding Pipeline", #you should edit this
    "user_name": "ubuntupunk", # change your Vectorshift username      
    }

    try: 
       #send the POST response to the API
        response = requests.post(url, headers=headers, data=data)

        #Check if the response was successful
        if response.status_code == 200:
            #Parse the response JSON
            response_json = response.json()

            if file_name:
                with open(file_name, 'w') as file:
                    json.dump(response_json, file, indent=1)
                    print(f"Results saved in {file_name}")

            if output_format.lower() == "txt" or output_format.lower() == "both":
                text_output = str(response_json).replace("\\n", "\n") # Replace escaped newlines
                print(Fore.GREEN + text_output + Style.RESET_ALL)

            if output_format.lower() == "json" or output_format.lower() == "both":
                print(json.dumps(response_json, indent=2))


        else:
           print(f"Error: {response.status_code} - {response.text}") 

    except Exception as e:
        print(f"An error occurred: {e}")


#Run the function
ask_question_and_save_results()
