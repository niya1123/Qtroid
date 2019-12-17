<%@ page language="java" contentType="text/html ; characterset=UTF-8" pageEncoding="UTF-8" %>

<!DOCTYPE html>

<html>
    <head>
        <title>To-Do-List</title>
    </head>
    <body>
        <% String userName = (String)request.getAttribute("userName"); %>
        こんにちは、"<%= userName %>"さん!

        <% if("Guest".equals(userName)) { %>
        <form method="POST" action="">
            何か入力してください: <input type="text" name="name">
            <button tyoe="submit">送信</button>
        </form>
        <% } %>
    </body>
</html>