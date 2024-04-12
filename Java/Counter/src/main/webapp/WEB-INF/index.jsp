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
<h1 class="text-warning bg-dark">Welcome User!</h1>
<p><a class= "badge bg-success" href= "/counter">Back to counter page</a></p>
<p><a class= "badge bg-primary" href= "/counterby2">Back to counter by 2 </a></p>
<hr>
<form action="/reset" method= "post">
<button class="btn btn-danger" >Reset <c:out value="${reset }"></c:out></button>
</form>
</body>
</html>