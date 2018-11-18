package com.iiits.doca.team.docaassistant;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;
import okio.ByteString;

import static java.lang.Thread.sleep;

public class Main3Activity extends AppCompatActivity {
    private TextView tv2;
    protected static Session session;
    protected static String uid;
    protected RecyclerView rcv;
    private OkHttpClient client;
    private fidadapter adp;
    protected static WebSocket ws;

    private final class EchoWebSocketListener extends WebSocketListener {
        private static final int i = 1000;

        @Override
        public void onMessage(WebSocket webSocket, final String text) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {

                    try {
                        JSONObject jo = new JSONObject(text);
                        String msg = jo.getString("message");
                        tv2.setText(msg);
                        int in = jo.getInt("pid");

                        if (in == 2) {
                            adp=new fidadapter(getApplicationContext(),2);
                            rcv.setAdapter(adp);

                        } else if (in == 1) {

                            adp=new fidadapter(getApplicationContext(),1);
                            rcv.setAdapter(adp);


                        }else if(in==3){
                            Intent myIntent = new Intent(Main3Activity.this, MainActivity.class);
                            Main3Activity.this.startActivity(myIntent);
                        }
                        else {
                            adp=new fidadapter(getApplicationContext(),0);
                            rcv.setAdapter(adp);

                        }

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }


                }

        });
        }

        @Override
        public void onMessage(WebSocket webSocket, ByteString bytes) {
            output("Receiving bytes : " + bytes.hex());
        }

        @Override
        public void onClosing(WebSocket webSocket, int code, String reason) {
            webSocket.close(i, null);
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
        setContentView(R.layout.activity_main3);
        session = new Session(getApplicationContext());
        tv2=findViewById(R.id.msg);
        client = new OkHttpClient();
        start();
        rcv=findViewById(R.id.rcv);
        rcv.setLayoutManager(new LLMW(this,LinearLayoutManager.VERTICAL,true));
        adp=new fidadapter(this,0);
        rcv.setAdapter(adp);


    }
    private void output(final String txt) {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                tv2.setText(txt);
            }
        });
    }
    private void start() {
        Request request = new Request.Builder().url("ws://10.0.34.36:8000/fg/").build();
        Main3Activity.EchoWebSocketListener listener = new Main3Activity.EchoWebSocketListener();
        ws = client.newWebSocket(request, listener);
        client.dispatcher().executorService().shutdown();
    }
}
