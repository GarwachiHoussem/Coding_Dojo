<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<%@ page isErrorPage="true"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Song</title>
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="/css/style.css">

<!-- change to match your file/naming structure -->
<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
</head>
<body class="image2">


	<h1>Describe your profile</h1>
	<form:form action="/songs/${song.id}/edit" method="put"
		modelAttribute="song">
		<div>
			<form:label path="title">Title: </form:label>
			<br />
			<form:errors path="title" class="text-danger" />
			<form:input style="width:250px;" path="title" />
		</div>

		<div>
			<form:label path="genre">Genre: </form:label>
			<br />
			<form:errors path="genre" class="text-danger" />
			<form:input style="width:250px;" path="genre" />
		</div>

		<div>
			<form:label path="lyrics">Add your lyrics: </form:label>
			<br />
			<form:errors path="lyrics" class="text-danger" />
			<form:textarea style="width:250px;" rows="3" path="lyrics" />
		</div>

		<div>
			<input type="submit" value="Submit" />
		</div>
	</form:form>

	<a href="/songs">Cancel</a>
	<form action="/songs/${song.id}/delete" method="post">
		
		<button type="submit" class="btn btn-danger" type="hidden"
			name="_method" value="delete">Delete</button>

	</form>
</body>
</html>