import pyttsx3
import PyPDF3


# this is to open the pdf book in reading mode
book = open('A-Little-Princess.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)  # initialising
pages = pdfReader.numPages  # this is for counting the numbers in the pdf book given
print(pages)  # printing the number of pages
speaker = pyttsx3.init()  # initialzing the speaker
# running a loop from a page number to the end of the pdf
for page_num in range(5, pages):
    page = pdfReader.getPage(5)  # getting the page
    text = page.extractText()  # extracting the text to read
    speaker.say(text)  # the speaker to read out the text
    speaker.runAndWait()  # speaker to run
speaker.stop()  # this is to stop the speaker after completing the task
