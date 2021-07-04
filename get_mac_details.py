import requests
import sys


def get_mac_details(get_url):
    try:
        mac_address = sys.argv[1]
        get_url += mac_address
        res =  requests.get(url=get_url)

        api_result = res.json()

        return api_result["vendorDetails"].get("companyName")
    except Exception as _e:
        print(f"Exception in getting the company name: {_e}")
        return None




if __name__ == "__main__":

    get_url = "https://api.macaddress.io/v1?apiKey=at_0wTH4bbyRfos4Bf8x04poMaKipGXV&output=json&search="
    
    company_name = get_mac_details(get_url)
    print(company_name)
