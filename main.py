################################
#          TO-DO
#   • Create the function the parses through rhymeSections and separates the rhymes by "," and adds the individual rhymes into the rhymes array
#       Currently - main.py groups based on syllables but has no way of separating by individual rhyme



import requests, bs4, sys
import subprocess

rhymes = []

def main(word):
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

    return rhymes

# DEBUG PURPOSES
# Opens a console that prints out whatever is within rhymes[index]
#subprocess.Popen(['start','cmd','/k','echo',rhymes[1]], shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, text = True)