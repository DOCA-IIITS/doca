package com.iiits.doca.team.docaassistant;

public class Doctor_model {
    private String Dname;
    private  String Ddp;
    private float Drating;
    private  String spec;
    private String location;
    public Doctor_model(String Dname,String Ddp,float Drating,String spec,String location){
        this.Dname=Dname;
        this.Ddp=Ddp;
        this.Drating=Drating;
        this.spec=spec;
        this.location=location;
    }
    public void setDoctor_Data(String Dname,String Ddp,float Drating,String spec,String location){
        this.Dname=Dname;
        this.Ddp=Ddp;
        this.Drating=Drating;
        this.spec=spec;
        this.location=location;
    }
    public String getDname(){
        return this.Dname;
    }
    public String getDdp(){
        return this.Ddp;
    }

    public float getDrating() {
        return Drating;
    }

    public String getSpec() {
        return spec;
    }

    public String getLocation() {
        return location;
    }
}
