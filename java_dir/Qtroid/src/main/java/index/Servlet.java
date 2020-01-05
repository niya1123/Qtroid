package index;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.sql.*;
import org.json.JSONObject;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.annotation.WebServlet;

@WebServlet("/json")
public class Servlet extends HttpServlet {


    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        
        resp.setContentType("text/html; charset=UTF-8"); //①ブラウザへ渡す情報の文字コードを指定

        PrintWriter out = resp.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("</head>");
        out.println("<body>");
        JSONObject json = new JSONObject();
        json.put("name","Taro");
        json.put("age",22);
        json.put("birthday","12/14");
        out.println(json);
        out.println("</body>");
        out.println("</html>");
    }

}