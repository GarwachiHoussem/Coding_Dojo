<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8" />
<title>show one</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
	rel="stylesheet"
	integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
	crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body class="image1">
	<div class="bg-black text-white bg-opacity-25">
		<h1>${song.title}</h1>
		<%--     <h2>Genre music played: ${song.person.username}</h2> --%>
		<h4>Genre: ${song.genre}</h4>
		<p>
			Describe of your skills: <br> ${song.lyrics}
		</p>

		<a  class="btn btn-success" href="/songs/${song.id }/edit">Modify</a>
	</div>
</body>
</html>
