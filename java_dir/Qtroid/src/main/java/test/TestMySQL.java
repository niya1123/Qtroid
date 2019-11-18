package test;
import java.sql.*;

/**
 * TestMySQL
 */
public class TestMySQL {

    public static void main(String[] args) {
        String msg = "";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/qiita_rank?autoReconnect=true&useSSL=false", "user", "userpass");
            Statement stmt = con.createStatement();

            String sqlStr = "SELECT * FROM tag_ranking";

            ResultSet rs = stmt.executeQuery(sqlStr);

            while(rs.next()){
                // レコードの値
                int id = rs.getInt("ranking");
                String name = rs.getString("tag_name");
         
                //表示
                System.out.println(id + ":" + name);
            }

            System.out.println("hope outprint.");

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