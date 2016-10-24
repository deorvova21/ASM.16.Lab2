<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="add_descendant">
Имя: <input type=text name=name value="{1}"><br>
Вид:
<select name=discipline value="{2}">
  <option>Женщины</option>
  <option>Мужчины</option>
  <option>Пары</option>
  <option>Танцы</option>
</select><br>
Тренер: <input type=text name=coach value="{3}"><br>
<br>
<input type=submit value="Сохранить">
<br>
<a href="?student={0}">Назад</a>
</form>