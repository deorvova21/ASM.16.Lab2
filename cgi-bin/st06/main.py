from .group import *

Gr = Group()

list = [
["Добавить студента", Gr.read],
["Изменить информацию о студенте", Gr.change],
["Удалить студента ", Gr.delete],
["Вывести на экран список группы", Gr.write],
["Записать в файл список", Gr.write_file],
["Считать из файла список", Gr.read_file],
["Очистить даные в списке", Gr.clear]
]

def main():
        try:
                i=1
                print("Введите номер действия")
                for o in list:
                        print(i, o[0])
                        i+=1
                print("Для возврата в предыдуще меню нажмите 0")    
                k = int(input())
                if (k==0): return
                print("")
                list[k-1][1]()
                print("")
                main()
        except:
                print("Введено некорректное значение")
                main()



                
                        
                
                        
