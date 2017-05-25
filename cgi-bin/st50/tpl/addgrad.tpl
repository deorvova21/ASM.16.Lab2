<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="addgrad">
<table> 
<caption><b>Добавление выпускника<b></caption>
<tr>
<td> Имя: </td> <td><input type=text name=name value="{1}"></td>
<td rowspan="3"> <input type=submit value="Добавить" style="width:100px;height:70px"> </td>
</tr>
<tr>
<td>Год: </td> <td><input type=text name=year value="{2}"></td>
</tr>
<tr>
<td>Диплом: </td> <td> <input type=text name=dipl value="{3}"></td>
</tr>
</table>
</form>
<a href="?student={0}">Назад</a>