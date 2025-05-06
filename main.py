# TO-DO
# Design GUI
# Make script state how many syllables each section contains
# Display the words in the GUI
# Create an input section for the user to type the word they want the rhyme for


import requests, bs4, sys
import subprocess

rhymes = []

def main(word):
    print(f"URL: https://www.rhymezone.com/r/rhyme.cgi?Word={word}&typeofrhyme=perfect&org1=syl&org2=l&org3=y")
    res = requests.get(f"https://www.rhymezone.com/r/rhyme.cgi?Word={word}&typeofrhyme=perfect&org1=syl&org2=l&org3=y")
    try:
        res.raise_for_status()
    except Exception as exc:
        print("There was a problem: %s" % (exc))

    # Scrape the page to return all of the rhymes
    rhymeZone = bs4.BeautifulSoup(res.text, "html.parser")
    # Save these sections to elems
    rhymeSections = rhymeZone.select('.contbreak')
    # Detect if rhymes are already present. If they are, remove them to include the new rhyme words
    if rhymes.__len__ != 0:
        rhymes.clear()
    # Parse through each rhyme in the list and add it to the rhyme array
    for rhyme in rhymeSections:
        rhymes.append(rhyme.getText().split(":")[1])

    print(rhymes[0])

# DEBUG PURPOSES
# Opens a console that prints out whatever is within rhymes[index]
#subprocess.Popen(['start','cmd','/k','echo',rhymes[1]], shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, text = True)