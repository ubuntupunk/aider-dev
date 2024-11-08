import json
import requests

def ask_question_and_save_results():

    #user input for the question and the file name
    question = input("Enter the question: ")
    file_name = input("Entering the file name: ")

    #define API details
    url = ""
    api_key = ""

    headers = {
      "Api-Key": api_key,
    },

    #Prepare the data payload with user input
    data = {
        "inputs": json.dumps({
            "input_1" : question
        }),
    "pipeline_name" : "untitled_pipeline_copy", #you can
    "user_name" : "ubuntupunk",      
    }

    try: 
       #send the POST response to the API
        response = requests.post(url, headers=headers, data=data)

        #Check if the response was successful
        if response.status_code == 200:
            #Parse the response jsON
            response_json = response.json()

        # Save the result to the specified file

            with open(file_name, 'w') as file:
                json_dump(respone.json, file, indents=1)
                print("results save in (file_name)")
        else:
           print(f"Error: {response.status_code} - {response.text}") 

    except Exception as e:
        print(f"An error occurred: (e)")


#Run the function
ask_question_and_save_results()


        
        
            

