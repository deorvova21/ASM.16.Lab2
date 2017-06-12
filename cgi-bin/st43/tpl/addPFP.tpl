<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="addPFP">
<table> 
<caption><b>Добавление профессионального футболиста<b></caption>
<tr>
<td> Имя: </td> <td><input type=text name=name value="{1}"></td>
<td rowspan="3"> <input type=submit value="Добавить" style="width:100px;height:70px"> </td>
</tr>

<tr>
<td>Фамилия: </td> <td><input type=text name=surname value="{2}"></td>
</tr>

<tr>
<td>Год рождения: </td> <td><input type=text name=year value="{3}"></td>
</tr>

<tr>
<td>Гражданство: </td> <td> <input type=text name=citizenship value="{4}"></td>
</tr>

<tr>
<td>Зарплата: </td> <td> <input type=text name=salary value="{5}"></td>
</tr>

<tr>
<td>Длительность контракта: </td> <td> <input type=text name=contract value="{6}"></td>
</tr>

</table>
</form>
<a href="?student={0}">Назад</a>

