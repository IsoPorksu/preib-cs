# Pre-IB CS project

This is my project for pre-IB computer science: a highly impractical Prisma store locator! By entering the name of a Prisma store (only Finnish stores are supported), you can get its latitude and longitude, which is so handy and useful!

## Specification
**Target grade level:** 3<br>
**Resource handling:** The code opens the JSON data file with a `with` statement, and is therefore closed automatically. Although the input/output cycle is run continuously until the program is exited, the data is only loaded once, at the start of the program.

## Test cases
1. input: `Zeppelin`; output: `The coordinates of Prisma Zeppelin are (64.901687, 25.538063).`
2. input: `Haaga`; output: `Sorry, there was no Prisma found at Haaga.`

## Explanation of the data format (dictionaries and JSON)
The data is stored in a dictionary format in a JSON file, which is a standard file type used to store data. A dictionary has two types of data: keys and values. The program checks whether the user’s input matches one of the store names stored before the colon in the file. If a match is found, the program reads the information stored after the colon, which, in this program, is a list containing the latitude and longitude of the store. The program then assigns the items in that list to the variables latitude and longitude.
