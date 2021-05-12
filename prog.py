import pyautogui as pg 
pg.alert( button = "Старт")
confirmation = pg.confirm("Вы хотите создать файл?" , "Создание файлов" , ("yes" , "no"))
if confirmation == "yes":
	name = pg.prompt("Введите название файла и укажите расширение." , "Создание файла")
	file = open(name , "w")
	record = pg.confirm("Вы хотите записать что-то в файл '{}'?".format(name) , "Создание паролей" , ("yes" , "no"))
	if record == 'yes':
		recording = pg.prompt("Введите то, что хотите записать в файл" , "Запись")
		file.write(recording)
	if record == 'no':
		pg.alert("Ладно.", button = "До связи")
else:
	pg.alert("До свидания!", button = "Goodbye, dude")