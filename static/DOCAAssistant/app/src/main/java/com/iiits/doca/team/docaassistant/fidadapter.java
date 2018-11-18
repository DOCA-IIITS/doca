package com.iiits.doca.team.docaassistant;
import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;

import android.text.Editable;
import android.text.TextWatcher;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;



public class fidadapter extends RecyclerView.Adapter<fidadapter.Dholder> {
    private Context cntx;
    protected  static int mls;

    fidadapter(Context context, int type) {
        cntx = context;
        mls = type;
    }

    @NonNull
    @Override
    public fidadapter.Dholder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater=LayoutInflater.from(cntx);
        if (mls==2) {
            View v = inflater.inflate(R.layout.pass, viewGroup, false);
            return new fidadapter.Dholder(v);
        }
        if (mls==1)
        {   View v = inflater.inflate(R.layout.eotp, viewGroup, false);
            return new fidadapter.Dholder(v);
        }
        View v = inflater.inflate(R.layout.fgid, viewGroup, false);
        return new fidadapter.Dholder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull Dholder dholder, int i) {
        final Button button=Dholder.btn1;


        if (mls==2){
            final TextView tv1=Dholder.tv1;
            final TextView tv2=Dholder.tv2;
            tv1.requestFocus();
        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {

                if(tv1.getText().toString().equals(tv2.getText().toString())){
                    JSONObject jb=new JSONObject();
                    try {
                        jb.put("pid",2);
                        jb.put("uid",Main3Activity.session.getfUid());
                        jb.put("pwd",tv1.getText().toString());
                        Main3Activity.ws.send(jb.toString());

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }

            }
        });}
        else if (mls==1){
            final TextView tv1=Dholder.tv1;
            tv1.requestFocus();
            final TextView tv2=Dholder.tv2;
            final TextView tv3=Dholder.tv3;
            final TextView tv4=Dholder.tv4;
            final TextView tv5=Dholder.tv5;
            final TextView tv6=Dholder.tv6;
            tv1.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){
                        tv2.requestFocus();
                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            tv2.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){
                        tv3.requestFocus();
                    }
                    else{
                        tv2.setText("");
                        tv1.requestFocus();

                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            tv3.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){
                        tv4.requestFocus();
                    }
                    else{
                        tv3.setText("");
                        tv2.requestFocus();

                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            tv4.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){
                        tv5.requestFocus();
                    }
                    else{
                        tv4.setText("");
                        tv3.requestFocus();

                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            tv4.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){
                        tv5.requestFocus();
                    }
                    else{
                        tv4.setText("");
                        tv3.requestFocus();

                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            tv5.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){
                        tv6.requestFocus();
                    }
                    else{
                        tv5.setText("");
                        tv4.requestFocus();

                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            tv6.addTextChangedListener(new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                }

                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                    if (count==1){

                    }
                    else{
                        tv6.setText("");
                        tv5.requestFocus();

                    }

                }

                @Override
                public void afterTextChanged(Editable s) {

                }
            });
            button.setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View view) {

                    String ji=tv1.getText().toString()+tv2.getText().toString()+tv3.getText().toString()+tv4.getText().toString()+tv5.getText().toString()+tv6.getText().toString();
                    JSONObject jb=new JSONObject();
                    try {
                        jb.put("pid",1);
                        jb.put("otp",ji);
                        jb.put("uid",Main3Activity.session.getfUid());
                        Main3Activity.ws.send(jb.toString());

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                    //Main2Activity.md.cletv1.paear();// Main2Activity.ws.send((String) button.getText());

            });
        }
        else{
            final TextView tv1=Dholder.tv1;
            button.setOnClickListener(new View.OnClickListener(){

                @Override
                public void onClick(View view) {
                    button.setEnabled(false);
                    String uid=tv1.getText().toString();
                    Main3Activity.session.setfUid(uid);
                    JSONObject jb=new JSONObject();
                    try {
                        jb.put("pid",0);
                        jb.put("uid",uid);
                        Main3Activity.ws.send(jb.toString());

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    //Main2Activity.md.clear();
                    // Main2Activity.ws.send((String) button.getText());
                }
            });
        }

    }

    @Override
    public int getItemCount() {
        return 1;
    }

    public static class Dholder extends RecyclerView.ViewHolder {
        static Button btn1;

        static TextView tv1;
        static TextView tv2;
        static TextView tv3;
        static TextView tv4;
        static TextView tv5;
        static TextView tv6;
        static TextView timer;

        public Dholder(@NonNull View itemView) {
            super(itemView);
            if(fidadapter.mls==2){
                tv1=(TextView)itemView.findViewById(R.id.fgnp);
                tv2=(TextView)itemView.findViewById(R.id.fgcpw);
                btn1=itemView.findViewById(R.id.fgbtn);

            }
            else if(fidadapter.mls==1){
                tv1=(TextView)itemView.findViewById(R.id.o1);
                tv2=(TextView)itemView.findViewById(R.id.o2);
                tv3=(TextView)itemView.findViewById(R.id.o3);
                tv4=(TextView)itemView.findViewById(R.id.o4);
                tv5=(TextView)itemView.findViewById(R.id.o5);
                tv6=(TextView)itemView.findViewById(R.id.o6);
                timer=(TextView)itemView.findViewById(R.id.timer);
                btn1=itemView.findViewById(R.id.otpbtn1);


            }
            else{
                tv1=(TextView)itemView.findViewById(R.id.fidtv1);
                btn1=itemView.findViewById(R.id.fbtn);



            }

        }
    }
}