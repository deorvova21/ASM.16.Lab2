<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="add_skater">
Имя: <input type=text name=name value="{1}"><br>
Вид:
<select name=discipline value="{2}">
  <option>Женщины</option>
  <option>Мужчины</option>
  <option>Пары</option>
  <option>Танцы</option>
</select><br>
<br>
<input type=submit value="Сохранить">
</form>
<a href="?student={0}">Назад</a>