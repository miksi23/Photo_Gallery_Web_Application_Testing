def read_image_urls(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        image_urls = [line.split(": ")[1].strip() for line in lines if line.startswith("Image ")]
    return image_urls

file1_name = 'Output_Chrome.txt'
file2_name = 'Output_Firefox.txt'

# function calls
file1_urls = read_image_urls(file1_name)
file2_urls = read_image_urls(file2_name)

# find unique URLs in each file
unique_urls_file1 = list(set(file1_urls) - set(file2_urls))
unique_urls_file2 = list(set(file2_urls) - set(file1_urls))

# display unique URLs
print("=" * 130)  # adding line at the beginning

print("URLs that exist only in", file1_name, "and not in", file2_name, ":")
if unique_urls_file1:
    for idx, url in enumerate(unique_urls_file1, start=1):
        print(f"{idx}. {url}")
else:
    print("None")

print("=" * 130)  # adding underline

print("URLs that exist only in", file2_name, "and not in", file1_name, ":")
if unique_urls_file2:
    for idx, url in enumerate(unique_urls_file2, start=1):
        print(f"{idx}. {url}")
else:
    print("None")

print("=" * 130)  # adding underline

print(f"Total images in {file1_name}: {len(file1_urls)}")
print(f"Total images in {file2_name}: {len(file2_urls)}")

print("=" * 130)  # adding underline

if unique_urls_file1 or unique_urls_file2:
    total_diff = len(unique_urls_file1) + len(unique_urls_file2)
    print(f"Total differences found: {total_diff}")
else:
    print("No differences found")

print("=" * 130)  # adding line at the end
