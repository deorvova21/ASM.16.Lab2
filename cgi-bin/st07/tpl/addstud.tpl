<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="addstud">

<table> 
<caption><b>Добавление студента<b></caption>
<tr>
<td> Имя: </td> <td><input type=text name=name value="{1}"></td>
<td rowspan="2"> <input type=submit value="Добавить" style="width:100px;height:50px"> </td>
</tr>
<tr>
<td>Год: </td> <td><input type=text name=year value="{2}"></td>
</tr>
</table>
</form>
<a href="?student={0}">Назад</a>