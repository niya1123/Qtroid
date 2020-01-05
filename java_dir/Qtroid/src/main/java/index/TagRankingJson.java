package index;


import java.io.IOException;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.sql.*;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.annotation.WebServlet;

@WebServlet("/json/tag_ranking")
public class TagRankingJson extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        
        resp.setContentType("text/html; charset=UTF-8"); //①ブラウザへ渡す情報の文字コードを指定

        PrintWriter out = resp.getWriter();
        JSONObject json = new JSONObject();

        try {   
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://mysql:3306/qiita_rank?characterEncoding=utf8&useSSL=false&serverTimezone=GMT%2B9:00", 
            "user", "userpass");
            Statement stmt = con.createStatement();
            String sqlStr = "SELECT * FROM tag_ranking";
            ResultSet rs = stmt.executeQuery(sqlStr);

            while(rs.next()){
                int tag_id = rs.getInt("tag_id");
                String tag_name = rs.getString("tag_name");
                String tag_url = rs.getString("tag_url");
                List<String> list = new ArrayList<String>();
                list.add(tag_name);
                list.add(tag_url);

                json.put(String.valueOf(tag_id), list);
                
            }

            out.println(json);

            rs.close();
            stmt.close(); 
            con.close();

        } catch (Exception e) {
            out.println("tag_ranking取得できんかったやよ～");
        }
        
    }
}