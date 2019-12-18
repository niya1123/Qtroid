package test;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.sql.*;
// import java.io.ProcessBuilder;
// import java.io.Process;


import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
// import javax.servlet.annotation.WebServlet;

// @WebServlet("/home/sample")
public class TestServlet extends HttpServlet {


    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        
        resp.setContentType("text/html; charset=UTF-8"); //①ブラウザへ渡す情報の文字コードを指定

        // try {
        //     PrintWriter out = resp.getWriter();
        //     ProcessBuilder pb = new ProcessBuilder("ping java_app");
        //     Process process = pb.start();
        //     process.waitFor();
        //     int ret = process.exitValue();   
        //     out.println(String.valueOf(ret));
        // } catch (Exception e) {
        //     PrintWriter out = resp.getWriter();
        //     out.println("コマンド失敗");
        // }

        try {

            
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://mysql:3306/qiita_rank?characterEncoding=utf8&useSSL=false&serverTimezone=GMT%2B9:00", 
            "user", "userpass");
            Statement stmt = con.createStatement();
            String sqlStr = "SELECT * FROM tag_ranking";

            ResultSet rs = stmt.executeQuery(sqlStr);
            //②htmlを出力
            
            PrintWriter out = resp.getWriter();
            out.println("<html>");
            out.println("<head>");
            out.println("</head>");
            out.println("<body>");
            out.println("<table border=\"1\">");
            out.println("<tr>");
            out.println("<th>ID</th>");
            out.println("<th>名前</th>");
            out.println("<th>URL</th>");
            out.println("</tr>");
            while(rs.next()){
                // レコードの値
                int id = rs.getInt("id");
                String name = rs.getString("tag_name");
                String url = rs.getString("tag_url");
                out.println("<tr>");
                out.println("<td>");
                out.println(String.valueOf(id));
                out.println("</td>");
                out.println("<td>");
                out.println(name);
                out.println("</td>");
                out.println("<td>");
                out.print("<a href=\"");
                out.print(url);
                out.print("\">");
                out.print(url);
                out.println("</a>");
                out.println("</td>");
                out.println("</tr>");
            }
            out.println("</body>");
            out.println("</html>");
            rs.close();
            stmt.close(); 
            con.close();
        } catch (Exception e) {
            PrintWriter out = resp.getWriter(); 
            out.println("<p>ダメでした </p>");
        }

    }

}