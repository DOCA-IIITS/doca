package com.iiits.doca.team.docaassistant;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.speech.RecognizerIntent;
import android.speech.tts.TextToSpeech;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.TextView;

//import com.iiits.doca.team.docaassistant.model;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.Locale;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;
import okio.ByteString;

import static java.lang.Thread.*;
import static java.lang.Thread.sleep;

public class Main2Activity extends AppCompatActivity implements TextToSpeech.OnInitListener {
    protected static Session session;
    private TextView tv3;
    private WebView wbv;
    protected RecyclerView rcv;
    protected  ArrayList md;
    private TextToSpeech tts;
    private Button btn;
    private OkHttpClient client;
    protected static WebSocket ws;
    private final int rc = 100;
    private int j = 0;
    protected outputAdapter adp;
    protected doctorAdapter adp2;
    private JSONObject jobj;
    protected static String state="intial";




    private final class EchoWebSocketListener extends WebSocketListener {
        private static final int i = 1000;

        @Override
        public void onMessage(WebSocket webSocket, final String text) {

            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    String uname;
                    try{
                        int s=md.size();
                        md.clear();
                        adp.notifyItemRangeRemoved(0,s);

                        jobj = new JSONObject(text);
                        uname=jobj.getString("gspeak");
                        if(jobj.has("ds")){
                            String dp="http://10.0.34.36:8000/static/uploads/roshanreddyy@gmail.com.png";
                            md.add(new Doctor_model("Dr.Avinash katariya",dp, (float) 5,"Eye","Sricity"));
                            md.add(new Doctor_model("Dr.Roshan Reddy",dp, (float) 5,"ENT","Sricity"));
                            rcv.setLayoutManager(new LLMW(getApplicationContext(),LinearLayoutManager.HORIZONTAL,false));
                            adp2=new doctorAdapter(getApplicationContext(),md);
                            rcv.setAdapter(adp2);

                        }
                        else {
                            int n = jobj.getInt("nopt");
                            for (int kt = 0; kt < n; ++kt) {
                                String t = jobj.getString("opt" + kt);
                                md.add(new model(t));

                            }
                            rcv.setLayoutManager(new LLMW(getApplicationContext(),LinearLayoutManager.VERTICAL,true));
                            adp = new outputAdapter(getApplicationContext(), md);
                            rcv.setAdapter(adp);
                        }
                        tv3.setText(uname);
                        speakOut(uname);
                    }
                    catch (JSONException e) {
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
    public void onInit(int status) {

        if (status == TextToSpeech.SUCCESS) {

            int result = tts.setLanguage(Locale.US);

            if (result == TextToSpeech.LANG_MISSING_DATA
                    || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported");
            }
        } else {
            Log.e("TTS", "Initilization Failed!");
        }

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Intent intent = getIntent();

        setContentView(R.layout.activity_main2);
        session = new Session(getApplicationContext());
        tv3 = (TextView) findViewById(R.id.gspeak);
        TextView output=findViewById(R.id.output);
        output.setText(session.getUid());
        tts = new TextToSpeech(this, (TextToSpeech.OnInitListener) this);
        rcv = (RecyclerView) findViewById(R.id.Av_Question);
        btn = (Button) findViewById(R.id.button3);
        client = new OkHttpClient();
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (j == 0) {
                    start();
                    j++;
                }

                promptSpeechInput();



            }
        });



        String udp = "http://10.0.52.247:8000/login/imgret/" + session.getUid() + ".png";
        md = new ArrayList<>();

        rcv.setLayoutManager(new LLMW(this,LinearLayoutManager.VERTICAL,true));
        tv3.setText(intent.getStringExtra("unm"));
        wbv = (WebView) findViewById(R.id.webView);
        wbv.loadUrl(udp);
        adp = new outputAdapter(this, md);
        rcv.setAdapter(adp);


    }
    private void speakOut(CharSequence text) {

        tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, "id1");
    }

    private void promptSpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.addFlags(Intent.FLAG_FROM_BACKGROUND);
        try {
            startActivityForResult(intent, rc);

        } catch (ActivityNotFoundException a) {

        }
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case rc: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    JSONObject jb=new JSONObject();
                    try {
                        jb.put("state",state);
                        jb.put("input",result.get(0));
                        jb.put("uid",session.getUid());
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                    ws.send(jb.toString());
                }
                break;
            }

        }

    }

    private void output(final String txt) {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                tv3.setText(txt);
            }
        });
    }





    private void start() {
        Request request = new Request.Builder().url("ws://192.168.43.126:8000/chatbot/").build();
        EchoWebSocketListener listener = new EchoWebSocketListener();
        ws = client.newWebSocket(request, listener);
        client.dispatcher().executorService().shutdown();
    }
}

