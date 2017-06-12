<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="edit">
<input type=hidden name=i value="{1}">
<table> 
<caption><b>Редактирование<b></caption>
<tr>
<td> Имя: </td> <td><input type=text name=name value="{2}"></td>
<td rowspan="2"> <input type=submit value="Изменить" style="width:100px;height:50px"> </td>
</tr>
<tr>
<td>Фамилия: </td> <td><input type=text name=surname value="{3}"></td>
</tr>

<tr>
<td>Год: </td> <td><input type=text name=year value="{4}"></td>
</tr>

<tr>
<td>Гражданство: </td> <td><input type=text name=citizenship value="{5}"></td>
</tr>
</table>
</form>
<a href="?student={0}">Назад</a>
