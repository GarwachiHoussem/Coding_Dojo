<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Title</title>
</head>
<body>
<fieldset>
    <h1> <c:out value="${Book.title}"></c:out></h1>
<p>Description:<c:out value="${Book.description}"></c:out> </p>
<p>Language:<c:out value="${Book.language}"></c:out> </p>
<p>Number of pages:<c:out value="${Book.pages}"></c:out> </p></fieldset>
</body>
</html>
