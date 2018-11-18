package com.iiits.doca.team.docaassistant;
import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
//import static java.lang.Thread.sleep;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;
import okio.ByteString;

import com.iiits.doca.team.docaassistant.Session;
public class MainActivity extends AppCompatActivity {
    private Session session;
    private TextView uid;
    private TextView pwd;
    private TextView output;
    private int j=0;
    private Button lgn;
    private OkHttpClient client;
    protected WebSocket ws;
    private JSONObject jobj;

    private final class EchoWebSocketListener extends WebSocketListener {
        private static final int i = 1000;
        @Override
        public void onOpen(WebSocket wb,Response rs){
            j=1;

        }


        @Override
        public void onMessage(WebSocket webSocket, String text) {
            String msg="msg",status="DocaLogout";

            try {
                 jobj = new JSONObject(text);
                 status=jobj.getString("resp");
                 if(status.equals("verfied")){
                     session.setUid(uid.getText().toString());
                     session.setPwd(pwd.getText().toString());
                     Intent myIntent = new Intent(MainActivity.this, Main2Activity.class);
                     MainActivity.this.startActivity(myIntent);
                 }
                 else{
                     msg=jobj.getString("reason");
                     output(msg);
                 }


            } catch (JSONException e) {
                e.printStackTrace();
            }





        }

        @Override
        public void onMessage(WebSocket webSocket, ByteString bytes) {
            output("Receiving bytes : " + bytes.hex());
        }

        @Override
        public void onClosing(WebSocket webSocket, int code, String reason) {
            webSocket.close(i, null);
            j=0;
            output("Closing : " + code + " / " + reason);
        }

        @Override
        public void onFailure(WebSocket webSocket, Throwable t, Response response) {
            output("Error : " + t.getMessage());
        }
        }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
                session=new Session(getApplicationContext());
                if(session.isLogin()==true){
                    Intent myIntent = new Intent(MainActivity.this, Main2Activity.class);
                    MainActivity.this.startActivity(myIntent);
                }

        setContentView(R.layout.activity_main);

        uid=(TextView)findViewById(R.id.uid);
        pwd=(TextView)findViewById(R.id.pwd);

        client = new OkHttpClient();
        start();
        lgn=(Button)findViewById(R.id.lnbtn);
        output=(TextView)findViewById(R.id.textView2);

        lgn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {

                try {
                    trylogin();
                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }

        });

        findViewById(R.id.btn2).setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent myIntent = new Intent(MainActivity.this, Main3Activity.class);
                MainActivity.this.startActivity(myIntent);
                ws.close(1000,"no use now");

            }

        });



    }
    private void start() {
        Request request = new Request.Builder().url("ws://192.168.43.126:8000/login/").build();
        EchoWebSocketListener listener = new EchoWebSocketListener();
        ws = client.newWebSocket(request, listener);
        client.dispatcher().executorService().shutdown();
    }
    private void trylogin() throws JSONException {

        JSONObject jo = new JSONObject();
        jo.put("uid", uid.getText());
        jo.put("pwd", pwd.getText());
        String str=jo.toString();
        output(str);
        ws.send(str);





    }


   public void output(final String txt) {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                output.setText(txt);
            }
        });
    }
}
































//