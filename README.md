# Applied-Python
#### *These are Python scripts written by me to save myself and my peers time when there are mission-essential and time sensitive tasks to complete.*

## 1. Flight Tracker
This script was created in order to sift through up to 100 flight numbers and passenger counts. There were some repeated flight numbers with updated passenger counts so this script iterated through this csv file and extracted each unique flight number with the most up to date passenger counts.

## 2. Data Cleansing
Upon receiving data to input into our enterprise system for managing equipment density lists (EDLs), I took a quick look at the data and realized it had to be cleaned for proper import. While the specific data was small enough to manually clean, I decided to write a script anyways. This script uses Pandas to specify fields that require integer only data, and extracts the proper integer from fields that contain integers with strings (ex: "113LBS" rewritten in it's place as 113)
