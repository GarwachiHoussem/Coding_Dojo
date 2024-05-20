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
    <title>Musicien</title>
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/css/style.css">

    <!-- change to match your file/naming structure -->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
</head>
<body class="image5">

<div class="container">
    <h1 class=" col-md-5 mt-4 bg-black text-white bg-opacity-25" >Describe your profile</h1>
    <form:form action="/songs/new" method="post" modelAttribute="song">
        <div class="form-group col-md-3 mt-4 bg-black text-white bg-opacity-25">
            <form:label path="title">Name:</form:label>
            <form:errors path="title" class="text-danger"/>
            <form:input style="width:250px;" path="title" class="form-control"/>
        </div>

        <div class="form-group col-md-3 mt-4 bg-black text-white bg-opacity-25">
            <form:label path="genre">Genre music played:</form:label>
            <form:errors path="genre" class="text-danger"/>
            <form:input style="width:250px;" path="genre" class="form-control"/>
        </div>

        <div class="form-group col-md-3 mt-4 bg-black text-white bg-opacity-25">
            <form:label path="lyrics">Describe of your skills:</form:label>
            <form:errors path="lyrics" class="text-danger"/>
            <form:textarea style="width:250px;" rows="3" path="lyrics" class="form-control"></form:textarea>
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>
    </form:form>
    <a href="/songs" class="btn btn-secondary">Cancel</a>
</div>

</body>
</html>
