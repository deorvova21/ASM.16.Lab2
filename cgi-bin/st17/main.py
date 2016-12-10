from .library import library

def main(q, selfurl):
  lib = library(q, selfurl)
  print ("Content-type: text/html; charset=utf-8\n\n")
  if 'action' in q:
    if (q['action'].value=="1"): 
      lib.printingList()
    if (q['action'].value=="2"):
      lib.addingBook()
      lib.editingElement()
    if (q['action'].value=="3"):
      lib.addingJournal()
      lib.editingElement()
    if (q['action'].value=="4"):
      lib.inputingBook()
    if (q['action'].value=="5"):
      lib.inputingJournal()
    if (q['action'].value=="6"):
      lib.editingElement()
    if (q['action'].value=="7"):
      lib.deletingElement()  
  else: 
    lib.printingList()



if __name__ == '__main__':
  main() 



