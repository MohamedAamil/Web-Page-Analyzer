"""
WebPageAnalyzer.py : Given an Url, gets the total sentences, words, unique words and top 5 words
"""

import PySimpleGUI as sg
from Utilities import get_html_content, parse_html,get_statistics, get_lines, get_words, get_top_words

Info = "The Webpage consists of the following information"


layout = [
    [sg.Text("WEB PAGE ANALYZER " , font = ("Simplified Arabic Fixed",15) , background_color = "white" ,text_color="black", pad = ((250,10) , (10,10)))],
    [sg.Text("Enter URL  : " , font = ("Simplified Arabic Fixed",13), pad = (40,20) , background_color = "white",text_color="black"),
     sg.InputText("" , size = (35 , 1), font = ("Simplified Arabic" , 13), key = 'url' , background_color= "white" , text_color= "black" ),sg.Button("OK",font=("Simplified Arabic Fixed", 14), key='done' , button_color =  "white on black")],
    [sg.Multiline("", font=("Simplified Arabic Fixed", 13), size=(70, 15), key='output' )],
    [sg.Image("Creator.png", size=(720, 50), background_color="white")]
]


def get_details(url):
    """
    Get the details from the Utilities.py
    :param url: string, Url
    """
    html = get_html_content(url)
    data = parse_html(html , 'p')
    statistics = get_statistics(data)
    display_details(statistics)

def display_details(stats):
    """
    To Display all the data gathered through statistics in Multiline
    :param stats: dict, word count,lines count,unique words count,top words
    """

    top = ""
    for word in stats["top_words"]:
        top = top + "\n" + word

    window['output'].print(Info,"\n\n")
    window['output'].print("Total Words : ", stats["word_count"])
    window['output'].print("Total Lines : ", stats["line_count"])
    window['output'].print("Total Unique Words : ", stats["unique_words"], "\n")
    window['output'].print("Top Words: \n", top)


if __name__ == '__main__':

    window = sg.Window("Web Page Analyzer", layout , background_color = "white" )
    while True:
        event,value = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'done':
            window.FindElement('output').Update('')
            if len(value["url"]) > 10:
                get_details(value["url"])

    window.close()