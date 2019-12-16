package test;

import java.io.PrintStream;
import java.sql.*;

/**
 * TestMySQL
 */
public class TestMySQL {

    public static void main(String[] args) {
        String msg = "";

        try {

            PrintStream out = new PrintStream(System.out, true, "UTF-8");
            out.println("try connect mysql driver...");
            Class.forName("com.mysql.cj.jdbc.Driver");
            out.println("now connect driver.");

            out.println("try connect mysql server...");
            Connection con = DriverManager.getConnection("jdbc:mysql://mysql:3306/qiita_rank?characterEncoding=utf8&useSSL=false&serverTimezone=GMT%2B9:00", 
            "user", "userpass");
            Statement stmt = con.createStatement();
            out.println("connected mysql!");

            String sqlStr = "SELECT * FROM tag_ranking";

            ResultSet rs = stmt.executeQuery(sqlStr);

            while(rs.next()){
                // レコードの値
                int id = rs.getInt("id");
                String name = rs.getString("tag_name");
         
                //表示
                out.println(id + ":" + name);
            }

            out.println("hope outprint.");

            rs.close();
            stmt.close(); 
            con.close();
        } catch (ClassNotFoundException e) {
            msg = "failed load driver for ClassNotFoundException."; 
            System.out.println(msg);
        }catch (Exception e){
            msg = "failed load driver for Exception.";
            System.out.println(msg);
          } 
        // System.out.println("Hello Gradle RUN World!");
    }
      
}