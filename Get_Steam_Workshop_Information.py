import requests

def get_file_details(publishedfileid):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"
    data = {
        "itemcount": 1,
        "publishedfileids[0]": publishedfileid
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def display_file_details(details):
    if not details or 'response' not in details or 'publishedfiledetails' not in details['response']:
        print("Unable to obtain file details")
        return

    file_info = details['response']['publishedfiledetails'][0]

    print("\nfile details:")
    print("-" * 40)
    for key, value in file_info.items():
        print(f"{key:25}: {value}")
    print("-" * 40)

def main():
    while True:
        publishedfileid = input("Please enter the Steam Published File ID（Or enter 'q' to exit）: ")
        if publishedfileid.lower() == 'q':
            break
        details = get_file_details(publishedfileid)
        if details:
            display_file_details(details)
        print("\n")

if __name__ == "__main__":
    main()
