package com.iiits.doca.team.docaassistant;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

public class Session {
    private SharedPreferences apref;
    public Session(Context cnt){
        apref=PreferenceManager.getDefaultSharedPreferences(cnt);
    }
    public void setUid(String uid){
        apref.edit().putString("uid",uid).commit();
    }
    public void setfUid(String uid){
        apref.edit().putString("fuid",uid).commit();
    }
    public void setPwd(String pwd){
        apref.edit().putString("paswd",pwd).commit();
    }
    public String getUid(){
        return apref.getString("uid","");
    }
    public String getfUid(){
        return apref.getString("fuid","");
    }
    public String getPwd(){
        return apref.getString("paswd","");
    }
    public void logoutS(){
        apref.edit().remove("paswd");
    }
    public Boolean isLogin(){
        if(apref.getString("paswd","ADOCA").equals("ADOCA"))
            return false;
        return true;
    }

}
