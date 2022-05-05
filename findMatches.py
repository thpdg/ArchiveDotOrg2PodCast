# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import sys

filename = ""
file_url = ""

if len(sys.argv) > 1:
    filename = sys.argv[1]
    file_url = sys.argv[2]

image_url = "https://ia903103.us.archive.org/20/items/InternetArchiveLogo_201805/internet%20archive%20logo.jpg"
if len(sys.argv) > 3:
    image_url = sys.argv[3]

print(f"Working with {filename} from {file_url}.")

regex = r"<td><a href=\"(.+?\.mp3)\">(.+?\.mp3)<\/a><\/td>"
title_regex = r"<h1>Files for (.+?)</h1>|$"

# Load file from archive.org into string
text_file = open(filename, "r")
file_data = text_file.read()

rss_title = re.findall(title_regex,file_data)
rss_title = rss_title[0]
print(f'Title is {rss_title}')

# Load RSS document template into string
text_file = open("RSSFeedDocumentTemplate.xml", "r")
output_document = text_file.read()
output_document = output_document.replace("%PODCAST_TITLE%", rss_title)
output_document = output_document.replace("%PODCAST_URL%",file_url)
output_document = output_document.replace("%PODCAST_IMG_URL%",image_url)

# Load RSS item template into string
text_file = open("RSSFeedItemTemplate.xml", "r")
output_item_template = text_file.read()

# test_str = ("<!DOCTYPE html>\n"
# "    ")

matches = re.finditer(regex, file_data, re.MULTILINE)

episode_entries = ""

def determine_date(source_string):
    date_string = "2022-05-04"
    return date_string

for matchNum, match in enumerate(matches, start=1):
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        episode_url = match.group(groupNum)
        print(f"URL is {episode_url}")
        
        # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

        episode_desc = match.group(groupNum)

        if len(match.groups())>1:
            episode_desc = match.group(2).replace('&amp;','&') 
            print (f"Desc found: {episode_desc}")

        episode_entry = output_item_template.replace("%EPISODE_TITLE%", episode_desc)
        episode_entry = episode_entry.replace("%EPISODE_SUMMARY%", episode_desc)
        episode_entry = episode_entry.replace("%EPISODE_DESCRIPTION%", episode_desc)
        episode_entry = episode_entry.replace("%SOUNDFILE_URL%", file_url + "/" + episode_desc)
        episode_entry = episode_entry.replace("%SOUNDFILE_DATE%", determine_date(episode_desc))

        # print(f"Episode Info:\n{episode_entry}")

        episode_entries += episode_entry + "\n"

        break

output_document = output_document.replace("%PODCAST_CONTENT%",episode_entries)

f = open(f"{rss_title}_rssoutput.rss", "w")
f.write(output_document)
f.close()