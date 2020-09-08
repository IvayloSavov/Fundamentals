file = input().split("\\")
file_name_extension = file[-1].split(".")
file_name = file_name_extension[0]
file_extension = file_name_extension[1]

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')
