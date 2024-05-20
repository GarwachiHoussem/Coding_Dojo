<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<%@ page isErrorPage="true"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard</title>
<!-- Bootstrap CSS -->
<link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<!-- Custom CSS -->
<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body class="image4">

	<div class="container">
		<h2 class="text-light " >
			Hello,
			<c:out value="${user.username}" />
			!🙋‍♂️ Your opportunity for recruitment starts here 😍. Operators
			contracting with us can see your data here 👌</h2>
				<br/>
		<a href="/logout" class="btn btn-danger">Logout</a>
	

		<h1 class="mt-4 text-light " >All Musicians</h1>
			<br/>
		<div class="row">
			<div class="col-md-6">
				<h2 class="mt-4 text-light ">Name</h2>
			</div>
			
			<div class="col-md-3">
				<h2 class="mt-4 text-light ">Genre</h2>
			</div>
		</div>
		<hr>
		<c:forEach items="${songs}" var="song">
			<div class="row text-white  ">
				<div class="col-md-6">
					<a href="/songs/${song.id}"><c:out value="${song.title}" /></a>
				</div>
				
				<div class="col-md-3">
					<p>
						<c:out value="${song.genre}" />
					</p>
				</div>
			</div>
		</c:forEach>
		<a href="/songs/new" class="btn btn-primary mt-3">Create a profile</a>
	</div>




</body>
</html>
