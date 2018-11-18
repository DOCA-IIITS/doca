package com.iiits.doca.team.docaassistant;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class doctorAdapter extends RecyclerView.Adapter<doctorAdapter.Dholder>{
    private Context cntx;
    private ArrayList<Doctor_model> mls;
    doctorAdapter(Context context, ArrayList<Doctor_model> list){
        cntx=context;
        mls=list;
    }

    @NonNull
    @Override
    public doctorAdapter.Dholder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater=LayoutInflater.from(cntx);
        View v=inflater.inflate(R.layout.doct,viewGroup,false);
        return new doctorAdapter.Dholder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull doctorAdapter.Dholder dholder, int i) {
        Doctor_model mdl=mls.get(i);
        final Button btn1=Dholder.btn1;
        final TextView tv1=Dholder.tv1;
        final TextView tv2=Dholder.tv2;
        final TextView tv3=Dholder.tv3;
        final TextView tv4=Dholder.tv4;
        final ImageView iv1=Dholder.iv1;

        tv1.setText(mdl.getDname());
        tv2.setText(mdl.getSpec());
        tv3.setText(""+mdl.getDrating());
        tv4.setText(mdl.getLocation());

        Picasso.with(cntx).load(mdl.getDdp()).into(iv1);


        try {
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(cntx.openFileOutput("config.txt", Context.MODE_PRIVATE));
            outputStreamWriter.write("asfg");
            outputStreamWriter.close();
        }
        catch (IOException e) {
            Log.e("Exception", "File write failed: " + e.toString());
            Main2Activity.ws.send("fail");
        }

    }

    @Override
    public int getItemCount() {
        return mls.size();
    }
    public static class Dholder extends RecyclerView.ViewHolder{
        static Button btn1;
        static TextView tv1;
        static TextView tv2;
        static TextView tv3;
        static  TextView tv4;
        static ImageView iv1;
        public Dholder(@NonNull View itemView) {
            super(itemView);
            btn1=itemView.findViewById(R.id.bookapp);
            tv1=itemView.findViewById(R.id.dname);
            tv2=itemView.findViewById(R.id.spec);
            tv3=itemView.findViewById(R.id.ratings);
            tv4=itemView.findViewById(R.id.location);
            iv1=itemView.findViewById(R.id.img1);





        }
    }
}
