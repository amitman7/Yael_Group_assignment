import requests

def gregorian_to_hebrew(*args, after_sunset=False):
    url = "https://www.hebcal.com/converter"

    if (type(args[0]) == str):
        g_date = args[0].split("-")
        gy, gm, gd = g_date[0], g_date[1], g_date[2]
    else :
        gy, gm, gd = args[0]
       
    params = {
        "cfg": "json",  
        "g2h": 1,  
        "gy": gy,
        "gm": gm, 
        "gd": gd,     
        "gs": 1 if after_sunset else 0,      
        "strict": 1,    
    }

    try:
        # API call
        response = requests.get(url, params=params)
        response.raise_for_status()  # error 

        response = response.json()
        
        day = response['heDateParts']['d'][::-1]
        month = response['heDateParts']['m'][::-1]
        year = response['heDateParts']['y'][::-1]
        hebrew_date = "Hebrew Date: " + year + "-" + month + "-" + day

        return hebrew_date
    
    except requests.exceptions.RequestException as e:
        return {"API call error": str(e)}



def main():
    print("Enter a date in the format of yyyy-mm-dd or enter a year, month, and day:")
    if (input("Enter a date? (True/False): ") == "True"):
        gregorian_date = input()
        # Check if the date is in the correct format
        if (gregorian_date.count("-") != 2 or len(gregorian_date) != 10 or gregorian_date[4] != "-" or gregorian_date[7] != "-"):
            print("Invalid date format. Please enter date in the format of yyyy-mm-dd.")
            exit()
    else:
        gregorian_date = (input("Enter year: "), input("Enter month: "), input("Enter day: "))

    after_sunset = input("After sunset? (True/False): ")

    result = gregorian_to_hebrew(gregorian_date, after_sunset)
    print('\n')
    print(result)
    print("-------------------------------------------------")

    

if __name__ == "__main__":
    main()

