import requests

# open the text file containing image URLs and names
with open('output.txt', 'r') as file:
    lines = file.readlines()

# initialize a list to store image data
image_data = []

# process each line in the file
for line in lines:
    parts = line.strip().split(": ")
    if len(parts) == 2:
        url = parts[1]
        url_parts = url.split('.')
        if len(url_parts) >= 2:
            image_name = url_parts[-2].split('/')[-1]  # extracts the image name from the URL
            image_data.append((image_name, url))
        else:
            print(f"Invalid URL format: {url}")

error_count = 0  # initialize error count

# iterate through the image data and check status codes
for image_name, url in image_data:
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code != 200:
            print("\n" + "="*50)
            print(f"STATUS CODE: {status_code}")
            print(f"Image Name: {image_name}")
            print("="*50 + "\n")
            error_count += 1
    except requests.exceptions.RequestException:
        pass

print(f"Total errors found: {error_count}")
