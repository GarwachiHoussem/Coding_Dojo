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
<title>show</title>
</head>
<body>
<h1>here's your imikuji</h1>
<p>In ${number} year you will live in ${city} with ${person} as your roommate,
${hobby} for a living. The next time see ${living}, you will have good luck.
Also, <c:out value="${say}"></c:out>  </p>

<a class="btn btn-primary" href= "/omikuji">Go Back</a>
</body>
</html>