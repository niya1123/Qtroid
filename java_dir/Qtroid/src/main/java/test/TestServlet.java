package test;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class TestServlet extends HttpServlet {


    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        
        String name = (String) req.getAttribute("userName");
        
        if(name == null || "".equals(name))
            req.setAttribute("userName", "Guest");
        
        String view_path = "/WEB-INF/views/index.jsp";

        RequestDispatcher dispatcher = req.getRequestDispatcher(view_path);

        dispatcher.forward(req, resp);
    }

    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
        
        req.setCharacterEncoding("utf-8");

        String name = req.getParameter("name");

        req.setAttribute("userName", name);

        doGet(req, resp);
    }
}