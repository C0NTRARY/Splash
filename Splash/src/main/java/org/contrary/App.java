package org.contrary;

/**
 * Created by avi6105 on 9/25/15.
 */

import static spark.Spark.*;

public class App {
    public static void main(String[] args){
        get("/hello", (req, res) -> "Hello World");
    }
}
