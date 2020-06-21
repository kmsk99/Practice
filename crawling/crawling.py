from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation


mbtis = ["enfj", "enfp", "entj", "entp", "esfj", "esfp", "estj", "estp", "infj", "infp", "intj", "intp", "isfj", "isfp", "istj", "istp"]

for mbti in mbtis:
    arguments = {"keywords_from_file":mbti+".txt", "output_directory":mbti, "no_directory":True, "limit":"10", "print_urls":True, "format":"jpg"}   #creating list of arguments
    paths = response.download(arguments) 
    print(paths) 