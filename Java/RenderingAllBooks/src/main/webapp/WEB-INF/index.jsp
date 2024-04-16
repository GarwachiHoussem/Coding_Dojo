<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>ALL BOOKS</title>
</head>
<body> 
<h1>All Books</h1>
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Language</th>
            <th>Number of Pages</th>
        </tr>
    </thead>
    <tbody> 
         <c:forEach var="book" items="${Book}">
        <tr>
         <td><c:out value="${book.id}"></c:out></td>
         <td><c:out value="${book.title}"></c:out></td>
         <td><c:out value="${book.language}"></c:out></td>
         <td><c:out value="${book.pages}"></c:out></td>
        </tr>
         </c:forEach> 
    </tbody>
</table>
    
</body>
</html>
