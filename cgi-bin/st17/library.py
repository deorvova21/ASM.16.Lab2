from .book import book
from .journal import journal

import pickle

filename = "cgi-bin/st17/data.txt"

class library:
    def __init__(self, q, selfurl):
        self.catalog = []
        self.q=q
        self.selfurl=selfurl
        self.readingList()

    def addingBook(self):
        newBook = book()
        self.catalog.append(newBook)
        self.id = len(self.catalog)-1

    def addingJournal(self):
        newJournal = journal()
        self.catalog.append(newJournal)
        self.id = len(self.catalog)-1


    def deletingElement(self):
        self.readingList()
        id=int(self.q['id'].value)
        self.catalog.pop(id)
        self.writingList()
        self.printingList()       

    def printingList(self):
        self.readingList()
        print('<p align=center><font color=#8B4513 size=18>Library Catalog</font></p>')
        if (len(self.catalog) == 0):
            print('<br><p align=center>There are no elements in Catalog</p>')
        else:
            id=0
            print("""<table border=2 width=900 bgcolor=#FFD39B align=center>
         <tr> <th width=100> Type </th>
	 <th width=150> Name </th>
	 <th width=80> Year </th>
	 <th> Month (for Journals only) </th>
	 <th> Number (for Journals only) </th>
	 <th> Location </th> 
	 <th width=130> Actions </th>
         </tr>""")
            for element in self.catalog:
                element.printing(id, self.q, self.selfurl)
                id=id+1
        print('''<br><br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<a href="{0}">Back</a> | <a href="{0}?student={1}&action=2">Add Book</a> | <a href="{0}?student={1}&action=3">Add Journal</a><br><br>'''.format(self.selfurl, self.q['student'].value))

    def editingElement(self):
        if 'id' in self.q:
            self.id=int(self.q['id'].value)
        self.catalog[self.id].change(self.id, self.q, self.selfurl)

    def inputingBook(self):
        id=int(self.q['id'].value)
        if (id==len(self.catalog)):
            self.addingBook()
        self.catalog[id].inputing(self.q)
        self.writingList()
        self.printingList()

    def inputingJournal(self):
        id=int(self.q['id'].value)
        if (id==len(self.catalog)):
            self.addingJournal()
        self.catalog[id].inputing(self.q)
        self.writingList()
        self.printingList()

    
    def writingList(self):
        with open(filename, 'wb') as f:
            pickle.dump(self.catalog, f)

    def readingList(self):
        try:
            with open(filename, 'rb') as f:
                self.catalog = pickle.load(f)
        except FileNotFoundError:
            pass         


            
        
