package com.iiits.doca.team.docaassistant;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class outputAdapter extends RecyclerView.Adapter<outputAdapter.Dholder> {
    private Context cntx;
    private ArrayList<model> mls;
    outputAdapter(Context context, ArrayList<model> list){
        cntx=context;
        mls=list;
    }
    @NonNull
    @Override
    public Dholder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater=LayoutInflater.from(cntx);
        View v=inflater.inflate(R.layout.question,viewGroup,false);
        return new Dholder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull Dholder dholder, int i) {
        final Button button=Dholder.btn2;
        model mdl=mls.get(i);
        button.setText((CharSequence) mdl.getQues());
        try {
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(cntx.openFileOutput("config.txt", Context.MODE_PRIVATE));
            outputStreamWriter.write(mdl.getQues());
            outputStreamWriter.close();
        }
        catch (IOException e) {
            Log.e("Exception", "File write failed: " + e.toString());
        }
        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                //Main2Activity.md.clear();

                JSONObject jo=new JSONObject();
                try {
                    jo.put("state",Main2Activity.state);
                    jo.put("input",button.getText());
                    jo.put("uid",Main2Activity.session.getUid());
                    Main2Activity.ws.send(jo.toString());
                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        });

    }

    @Override
    public int getItemCount() {
        return mls.size();
    }
    public static class Dholder extends RecyclerView.ViewHolder{
        static Button btn2;
        public Dholder(@NonNull View itemView) {
            super(itemView);
            btn2=itemView.findViewById(R.id.btn);
        }
    }

}
