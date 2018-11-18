package com.iiits.doca.team.docaassistant;

import android.content.Context;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;

public class LLMW extends LinearLayoutManager {
    public LLMW(Context context, int orientation, boolean reverseLayout) {
        super(context, orientation, reverseLayout);
    }

    @Override
    public void onLayoutChildren(RecyclerView.Recycler rclyr,RecyclerView.State stat){
        try{
            super.onLayoutChildren(rclyr,stat);
        }
        catch (IndexOutOfBoundsException e){
            Log.e("probe","i dont know it");
        }
    }
}
