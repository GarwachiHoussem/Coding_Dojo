<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
	rel="stylesheet"
	integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
	crossorigin="anonymous">
<meta charset="ISO-8859-1">
<title>Insert title here</title>

</head>
<body>
<h1>Send an imokuji!</h1>
<fieldset>
<form action="/processForm" method="POST">


<label>pick any number from 5 to 25:</label>
<input name="number" type = "number" min=5 max=25>
<br>
<label>Enter the name of any city:</label>
<input name="city" type = "text" maxlength="15">
<br>
<label>Enter the name of any real person:</label>
<input name="person" type = "text" maxlength="15">
<br>
<label>Enter the name of hobby:</label>
<input name="hobby" type = "text" maxlength="15">
<br>
<label>Enter any type of living thing:</label>
<input name="living" type = "text" maxlength="15">
<br>
<label>Say something nice to someone:</label>
<input name="say" type = "text" maxlength="15">
<br>
<label>Send and show a friend </label>
<br>
<input type="submit" class="btn btn-primary">

</form>
</fieldset>


</body>
</html>